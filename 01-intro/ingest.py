import requests
from sqlitesearch import TextSearchIndex

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

documents = []
for course in courses_raw:
    course_url = f'https://datatalks.club/faq{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()
    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)

print(f"Loaded {len(documents)} documents")

index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    id_field="id",
    db_path="faq.db"
)

index.fit(documents)
index.close()

print("Done. Index saved to faq.db")
