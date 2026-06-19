import requests
from minsearch import Index
from typing import TypedDict


class FAQDocument(TypedDict):
    """Shape of a single FAQ record used by retrieval and prompt building."""

    question: str
    section: str
    answer: str
    course: str
    doc_id: str


def load_faq_data() -> list[FAQDocument]:
    """Download every course's FAQ entries from the DataTalksClub site.

    Fetches the course directory, then each course's JSON feed, and flattens
    the results into a single list. The original ``id`` field is renamed to
    ``doc_id`` so the records can be safely upserted into SQLite (and other
    stores) without re-importing the same rows.
    """
    docs_url = 'https://datatalks.club/faq/json/courses.json'
    response = requests.get(docs_url)
    courses_raw = response.json()

    documents: list[FAQDocument] = []
    url_prefix = 'https://datatalks.club/faq'

    for course in courses_raw:
        course_url = f'{url_prefix}{course["path"]}'
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    for doc in documents:
        doc["doc_id"] = doc.pop("id")  # rename so SQLite uses it as a stable id and we don't reimport the same records

    return documents


def build_index(documents: list[FAQDocument]) -> Index:
    """Fit a minsearch :class:`~minsearch.Index` over the FAQ documents.

    ``question``, ``section`` and ``answer`` are full-text searched, while
    ``course`` is a keyword field used for exact filtering.
    """
    index = Index(
        text_fields=['question', 'section', 'answer'],
        keyword_fields=['course']
    )
    index.fit(documents)
    return index
