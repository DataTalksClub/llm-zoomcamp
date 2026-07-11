from dotenv import load_dotenv

load_dotenv()

from agent import faq_agent, SearchDeps
from ingest import build_index, load_faq_data


def main():
    # Download the FAQ and build the search index
    documents = load_faq_data()
    index = build_index(documents)

    # Inject the index into the agent via the dependency container
    deps = SearchDeps(index=index)

    # Ask a question. run_sync blocks until the agent is done;
    # the agent may call search multiple times before answering.
    question = 'I just discovered the course. Can I join it?'
    result = faq_agent.run_sync(question, deps=deps)

    print(result.output)


if __name__ == '__main__':
    main()
