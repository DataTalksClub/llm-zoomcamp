
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from rouge import Rouge

# Define the URL for the dataset
github_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main/04-monitoring/data/results-gpt4o-mini.csv'
url = f'{github_url}?raw=1'

# Load the dataset
df = pd.read_csv(url)

# Use only the first 300 documents
df = df.iloc[:300]

# Load the embeddings model
model_name = 'multi-qa-mpnet-base-dot-v1'
embedding_model = SentenceTransformer(model_name)

# Create the embeddings for the first LLM answer
answer_llm = df.iloc[0].answer_llm
embedding = embedding_model.encode(answer_llm)

# Print the first value of the resulting vector
print("First value of the resulting vector:", embedding[0])

# Initialize an empty list for the evaluations
evaluations = []

# Compute embeddings and dot products
for _, row in df.iterrows():
    emb_llm = embedding_model.encode(row['answer_llm'])
    emb_orig = embedding_model.encode(row['answer_orig'])
    dot_product = np.dot(emb_llm, emb_orig)
    evaluations.append(dot_product)

# Compute the 75th percentile of the scores
percentile_75 = np.percentile(evaluations, 75)
print("75th percentile of the dot product scores:", percentile_75)

# Function to normalize a vector
def normalize(v):
    norm = np.sqrt((v * v).sum())
    return v / norm

# Compute cosine similarity
cosine_similarities = []
for _, row in df.iterrows():
    emb_llm = normalize(embedding_model.encode(row['answer_llm']))
    emb_orig = normalize(embedding_model.encode(row['answer_orig']))
    cosine_similarity = np.dot(emb_llm, emb_orig)
    cosine_similarities.append(cosine_similarity)

# Compute the 75th percentile of the cosine similarities
percentile_75_cosine = np.percentile(cosine_similarities, 75)
print("75th percentile of the cosine similarities:", percentile_75_cosine)

# Initialize ROUGE scorer
rouge_scorer = Rouge()

# Get the record with doc_id=5170565b
record = df[df['document'] == '5170565b'].iloc[0]

# Compute ROUGE scores
scores = rouge_scorer.get_scores(record['answer_llm'], record['answer_orig'])[0]

# Print the F1 score for ROUGE-1
rouge_1_f1 = scores['rouge-1']['f']
print("F1 score for ROUGE-1:", rouge_1_f1)

# Compute the average ROUGE score for the same record
rouge_2_f1 = scores['rouge-2']['f']
rouge_l_f1 = scores['rouge-l']['f']
rouge_avg = (rouge_1_f1 + rouge_2_f1 + rouge_l_f1) / 3
print("Average ROUGE score for the record:", rouge_avg)

# Compute ROUGE scores for all records
rouge_scores = []

for _, row in df.iterrows():
    scores = rouge_scorer.get_scores(row['answer_llm'], row['answer_orig'])[0]
    rouge_1_f1 = scores['rouge-1']['f']
    rouge_2_f1 = scores['rouge-2']['f']
    rouge_l_f1 = scores['rouge-l']['f']
    rouge_avg = (rouge_1_f1 + rouge_2_f1 + rouge_l_f1) / 3
    rouge_scores.append(rouge_l_f1)

# Compute the average ROUGE-L score across all records
average_rouge_l = np.mean(rouge_scores)
print("Average ROUGE-L score across all records:", average_rouge_l)
