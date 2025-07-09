import json
import subprocess

from typing import Dict, Any, List, Optional


class MCPClient:
    def __init__(self, server_command: List[str]):
        """
        Initialize the FastMCP client.
        
        Args:
            server_command: Command to start the server (e.g., ["python", "server.py"])
        """
        self.server_command = server_command
        self.process = None
        self.request_id = 0
        self.available_tools = {}
        self.is_initialized = False
        
    def start_server(self):
        """Start the FastMCP server process"""
        self.process = subprocess.Popen(
            self.server_command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=0
        )
        print(f"Started server with command: {' '.join(self.server_command)}")
        
    def stop_server(self):
        """Stop the server process"""
        if self.process:
            self.process.terminate()
            self.process.wait()
            print("Server stopped")
            
    def _get_next_request_id(self) -> int:
        """Get the next request ID"""
        self.request_id += 1
        return self.request_id
        
    def _send_notification(self, method: str, params: Optional[Dict[str, Any]] = None):
        """Send a notification (no response expected)"""
        if not self.process:
            raise RuntimeError("Server not started")
            
        notification = {
            "jsonrpc": "2.0",
            "method": method
        }
        
        if params:
            notification["params"] = params
            
        # Send notification
        notification_str = json.dumps(notification) + "\n"
        self.process.stdin.write(notification_str)
        self.process.stdin.flush()
        
    def _send_request(self, method: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Send a JSON-RPC request to the server via stdin"""
        if not self.process:
            raise RuntimeError("Server not started")
            
        request = {
            "jsonrpc": "2.0",
            "id": self._get_next_request_id(),
            "method": method
        }
        
        if params:
            request["params"] = params
            
        # Send request
        request_str = json.dumps(request) + "\n"
        self.process.stdin.write(request_str)
        self.process.stdin.flush()
        
        # Read response
        response_str = self.process.stdout.readline().strip()
        if not response_str:
            raise RuntimeError("No response from server")
            
        response = json.loads(response_str)
        
        if "error" in response:
            raise Exception(f"Server error: {response['error']}")
            
        return response.get("result", {})
        
    def initialize(self) -> Dict[str, Any]:
        """Send initialize request to the server"""
        print("Sending initialize request...")
        
        result = self._send_request(
            "initialize",
            {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "roots": {"listChanged": True},
                    "sampling": {}
                },
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        )
        
        print(f"Initialize response: {result}")
        return result
        
    def initialized(self):
        """Send initialized notification to complete handshake"""
        print("Sending initialized notification...")
        
        self._send_notification("notifications/initialized")
        self.is_initialized = True
        
        print("Handshake completed successfully")

    def get_tools(self) -> List[Dict[str, Any]]:
        """Get available tools from the server"""
        if not self.is_initialized:
            raise RuntimeError("Client not initialized. Call initialize() and initialized() first.")
            
        print("Retrieving available tools...")
        
        result = self._send_request("tools/list")
        tools = result.get("tools", [])
        
        # Store tools for easy access
        self.available_tools = {tool["name"]: tool for tool in tools}
        
        print(f"Available tools: {list(self.available_tools.keys())}")
        return tools
        
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Call a specific tool with given arguments"""
        if not self.is_initialized:
            raise RuntimeError("Client not initialized. Call initialize() and initialized() first.")
            
        if tool_name not in self.available_tools:
            raise ValueError(f"Tool '{tool_name}' not available. Available tools: {list(self.available_tools.keys())}")
            
        print(f"Calling tool '{tool_name}' with arguments: {arguments}")
        
        result = self._send_request(
            "tools/call",
            {
                "name": tool_name,
                "arguments": arguments
            }
        )
        
        return result
        
    def list_available_tools(self):
        """Print information about available tools"""
        if not self.available_tools:
            print("No tools available. Call get_tools() first.")
            return
            
        print("\nAvailable Tools:")
        print("-" * 50)
        for name, tool in self.available_tools.items():
            print(f"Name: {name}")
            print(f"Description: {tool.get('description', 'No description')}")
            
            # Print input schema if available
            input_schema = tool.get('inputSchema', {})
            if input_schema.get('properties'):
                print("Parameters:")
                for param_name, param_info in input_schema['properties'].items():
                    param_type = param_info.get('type', 'unknown')
                    param_desc = param_info.get('description', 'No description')
                    print(f"  - {param_name} ({param_type}): {param_desc}")
            
            print("-" * 50)


def convert_mcp_tool_to_function_format(mcp_tool):
    """
    Convert MCP tool format to function format.
    
    Args:
        mcp_tool: Tool object or dict with MCP format
    
    Returns:
        dict: Tool in function format
    """
    # Handle both Tool objects and dictionaries
    if hasattr(mcp_tool, 'name'):
        # It's a Tool object
        name = mcp_tool.name
        description = mcp_tool.description
        input_schema = mcp_tool.inputSchema
    else:
        # It's a dictionary
        name = mcp_tool['name']
        description = mcp_tool['description']
        input_schema = mcp_tool['inputSchema']
    
    # Clean up description - remove docstring formatting
    clean_description = description.split('\n\n')[0] if '\n\n' in description else description
    clean_description = clean_description.strip()
    
    # Convert the tool format
    function_tool = {
        "type": "function",
        "name": name,
        "description": clean_description,
        "parameters": {
            "type": "object",
            "properties": {},
            "required": input_schema.get('required', []),
            "additionalProperties": False
        }
    }
    
    # Convert properties
    if 'properties' in input_schema:
        for prop_name, prop_info in input_schema['properties'].items():
            function_tool["parameters"]["properties"][prop_name] = {
                "type": prop_info.get('type', 'string'),
                "description": prop_info.get('description', f"{prop_name.replace('_', ' ').title()}")
            }
            
            # Add title as description if no description exists
            if 'title' in prop_info and 'description' not in prop_info:
                function_tool["parameters"]["properties"][prop_name]["description"] = prop_info['title']
    
    return function_tool


def convert_tools_list(mcp_tools):
    """
    Convert a list of MCP tools to function format.
    
    Args:
        mcp_tools: List of MCP tools
    
    Returns:
        list: List of tools in function format
    """
    return [convert_mcp_tool_to_function_format(tool) for tool in mcp_tools]



class MCPTools:
    def __init__(self, mcp_client):
        self.mcp_client = mcp_client
        self.tools = None
    
    def get_tools(self):
        if self.tools is None:
            mcp_tools = self.mcp_client.get_tools()
            self.tools = convert_tools_list(mcp_tools)
        return self.tools

    def function_call(self, tool_call_response):
        function_name = tool_call_response.name
        arguments = json.loads(tool_call_response.arguments)

        result = self.mcp_client.call_tool(function_name, arguments)

        return {
            "type": "function_call_output",
            "call_id": tool_call_response.call_id,
            "output": json.dumps(result, indent=2),
        }