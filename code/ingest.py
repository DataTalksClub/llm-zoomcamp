import requests
from minsearch import Index

# load json object from datatalks.clue website.
# json objects ingestions alternatives:
# Will investigate 'Workshop on Data Ingestion' around 03-orchestration
#   requests:	Quick testing and small files.
#   dlt:	    Production-grade pipelines and automated loading.
#   Pandas:	    Data cleaning and structured datasets.
#   ijson:	    Extremely large JSON objects (memory efficient).


def load_faq_data():
    # Injection from website with clean and structured json data
    docs_url = 'https://datatalks.club/faq/json/courses.json'
    response = requests.get(docs_url)
    #print(response.status_code)
    courses_raw = response.json()

    documents = []
    url_prefix = 'https://datatalks.club/faq'

    for course in courses_raw:
        course_url = f'{url_prefix}{course["path"]}'
        course_response = requests.get(course_url)
        # raise error if there is wrong status, to prevent inject wrong json contents into documents
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    return documents

def build_index(documents):
    index = Index(
        text_fields=['question', 'section', 'answer'],
        keyword_fields=['course']
    )
    index.fit(documents)
    return index