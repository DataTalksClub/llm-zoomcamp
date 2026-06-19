from openai import OpenAI
from minsearch import Index

from ingest import FAQDocument

INSTRUCTIONS = '''
Your task is to answer questions from course participants
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
    """Retrieval-augmented chat assistant over the course FAQ.

    Wires together a minsearch index (retrieval) and an OpenAI client
    (generation) to answer participant questions using only the FAQ
    entries of a single course.
    """

    def __init__(
        self,
        index: Index,
        llm_client: OpenAI,
        instructions: str = INSTRUCTIONS,
        prompt_template: str = PROMPT_TEMPLATE,
        course: str = 'llm-zoomcamp',
        model: str = 'gpt-5.4-mini',
    ) -> None:
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model

    def search(self, query: str, num_results: int = 5) -> list[FAQDocument]:
        """Run a boosted search for ``query`` within this course's FAQ set."""
        boost_dict: dict[str, float] = {'question': 3.0, 'section': 0.5}
        filter_dict: dict[str, str] = {'course': self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict
        )

    def build_context(self, search_results: list[FAQDocument]) -> str:
        """Render search results into the plain-text block fed to the LLM."""
        lines: list[str] = []

        for doc in search_results:
            lines.append(doc['section'])
            lines.append('Q: ' + doc['question'])
            lines.append('A: ' + doc['answer'])
            lines.append('')

        return '\n'.join(lines).strip()

    def build_prompt(self, query: str, search_results: list[FAQDocument]) -> str:
        """Fill the prompt template with the question and its retrieved context."""
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, prompt: str) -> str:
        """Send ``instructions`` + ``prompt`` to the model and return its reply."""
        input_messages: list[dict[str, str]] = [
            {'role': 'developer', 'content': self.instructions},
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text

    def rag(self, query: str) -> str:
        """Answer ``query`` end-to-end: retrieve -> build prompt -> generate."""
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer
