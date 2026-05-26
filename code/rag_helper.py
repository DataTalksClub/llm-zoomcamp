'''this is the module to help building RAGBase class'''

# Module variables
INSTRUCTIONS = '''
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
'''

PROMPT_TEMPLATE = '''
QUESTION: {question}

CONTEXT:
{context}
'''.strip()

class RAGBase:
    def __init__(
        self,
        index,  #need by search()
        llm_client,  #need by llm() from rag()
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        course='llm-zoomcamp', #need by search()
        model='gpt-5.4-mini'  #need by llm() from rag()
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model    

    def search(self, query, num_results=5):
        # Rag 1: Find relevent content related to query
        ## in RAGBase, we are getting relevent contents via text index

        boost_dict = {'question': 3.0, 'section': 0.5}
        filter_dict = {'course': self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict
        )  # a list of documentation dicts

    def build_context(self, search_results):
        # convert search results: list of documentation dicts to a multiple-lines string
        lines = []

        for doc in search_results:
            lines.append(doc['section'])
            lines.append('Q: ' + doc['question'])
            lines.append('A: ' + doc['answer'])
            lines.append('')

        return '\n'.join(lines).strip()   # multiple lines string

    def build_prompt(self, query, search_results):
        # Rag 2: Build prompt with query and search_results

        context = self.build_context(search_results)

        # There are two parameters in prompt template string, use str.format to pupulate the final prompt
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, prompt):
        # get responses by invoke llm_client.resposnes
        input_messages = [
            {'role': 'developer', 'content': self.instructions},
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text

    def rag(self, query):
        # RAG has 3 steps: 
        # RAG 1: Search relevent contents for query (build search function) 
        search_results = self.search(query)
        # Rag 2: Build prompt by combining query and relevent contents found by search function from RAG 1
        prompt = self.build_prompt(query, search_results)
        # Rag 3: get result by calling llm_client with prompt from Rag2
        answer = self.llm(prompt)
        return answer
    
class RAGVector(RAGBase):

    def __init__(self, embedder, **kwargs):
        super().__init__(**kwargs)
        self.embedder = embedder

    def search(self, query, num_results=5):
        query_vector = self.embedder.encode(query)
        filter_dict = {'course': self.course}

        return self.index.search(
            query_vector,
            num_results=num_results,
            filter_dict=filter_dict
        )
