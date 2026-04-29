1. **Precision at k (P@k)**:
   - Measures the number of relevant documents in the top k results.
   - Formula: `P@k = (Number of relevant documents in top k results) / k`

2. **Recall**:
   - Measures the number of relevant documents retrieved out of the total number of relevant documents available.
   - Formula: `Recall = (Number of relevant documents retrieved) / (Total number of relevant documents)`

3. **Mean Average Precision (MAP)**:
   - Computes the average precision for each query and then averages these values over all queries.
   - Formula: `MAP = (1 / |Q|) * Σ (Average Precision(q))` for q in Q

4. **Normalized Discounted Cumulative Gain (NDCG)**:
   - Measures the usefulness, or gain, of a document based on its position in the result list.
   - Formula: `NDCG = DCG / IDCG`
     - `DCG = Σ ((2^rel_i - 1) / log2(i + 1))` for i = 1 to p
     - `IDCG` is the ideal DCG, where documents are perfectly ranked by relevance.

5. **Mean Reciprocal Rank (MRR)**:
   - Evaluates the rank position of the first relevant document.
   - Formula: `MRR = (1 / |Q|) * Σ (1 / rank_i)` for i = 1 to |Q|

6. **F1 Score**:
   - Harmonic mean of precision and recall.
   - Formula: `F1 = 2 * (Precision * Recall) / (Precision + Recall)`

7. **Area Under the ROC Curve (AUC-ROC)**:
   - Measures the ability of the model to distinguish between relevant and non-relevant documents.
   - AUC is the area under the Receiver Operating Characteristic (ROC) curve, which plots true positive rate (TPR) against false positive rate (FPR).

8. **Mean Rank (MR)**:
   - The average rank of the first relevant document across all queries.
   - Lower values indicate better performance.

9. **Hit Rate (HR) or Recall at k**:
   - Measures the proportion of queries for which at least one relevant document is retrieved in the top k results.
   - Formula: `HR@k = (Number of queries with at least one relevant document in top k) / |Q|`

10. **Expected Reciprocal Rank (ERR)**:
    - Measures the probability that a user finds a relevant document at each position in the ranked list, assuming a cascading model of user behavior.
    - Formula: `ERR = Σ (1 / i) * Π (1 - r_j) * r_i` for j = 1 to i-1
      - Where `r_i` is the relevance probability of the document at position i.
