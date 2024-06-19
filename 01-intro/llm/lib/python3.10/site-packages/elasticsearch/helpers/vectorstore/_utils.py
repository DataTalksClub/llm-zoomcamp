#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from enum import Enum
from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    import numpy as np
    import numpy.typing as npt

Matrix = Union[
    List[List[float]], List["npt.NDArray[np.float64]"], "npt.NDArray[np.float64]"
]


class DistanceMetric(str, Enum):
    """Enumerator of all Elasticsearch dense vector distance metrics."""

    COSINE = "COSINE"
    DOT_PRODUCT = "DOT_PRODUCT"
    EUCLIDEAN_DISTANCE = "EUCLIDEAN_DISTANCE"
    MAX_INNER_PRODUCT = "MAX_INNER_PRODUCT"


def maximal_marginal_relevance(
    query_embedding: List[float],
    embedding_list: List[List[float]],
    lambda_mult: float = 0.5,
    k: int = 4,
) -> List[int]:
    """Calculate maximal marginal relevance."""

    try:
        import numpy as np
    except ModuleNotFoundError as e:
        _raise_missing_mmr_deps_error(e)

    query_embedding_arr = np.array(query_embedding)

    if min(k, len(embedding_list)) <= 0:
        return []
    if query_embedding_arr.ndim == 1:
        query_embedding_arr = np.expand_dims(query_embedding_arr, axis=0)
    similarity_to_query = _cosine_similarity(query_embedding_arr, embedding_list)[0]
    most_similar = int(np.argmax(similarity_to_query))
    idxs = [most_similar]
    selected = np.array([embedding_list[most_similar]])
    while len(idxs) < min(k, len(embedding_list)):
        best_score = -np.inf
        idx_to_add = -1
        similarity_to_selected = _cosine_similarity(embedding_list, selected)
        for i, query_score in enumerate(similarity_to_query):
            if i in idxs:
                continue
            redundant_score = max(similarity_to_selected[i])
            equation_score = (
                lambda_mult * query_score - (1 - lambda_mult) * redundant_score
            )
            if equation_score > best_score:
                best_score = equation_score
                idx_to_add = i
        idxs.append(idx_to_add)
        selected = np.append(selected, [embedding_list[idx_to_add]], axis=0)
    return idxs


def _cosine_similarity(X: Matrix, Y: Matrix) -> "npt.NDArray[np.float64]":
    """Row-wise cosine similarity between two equal-width matrices."""

    try:
        import numpy as np
        import simsimd as simd
    except ModuleNotFoundError as e:
        _raise_missing_mmr_deps_error(e)

    if len(X) == 0 or len(Y) == 0:
        return np.array([])

    X = np.array(X)
    Y = np.array(Y)
    if X.shape[1] != Y.shape[1]:
        raise ValueError(
            f"Number of columns in X and Y must be the same. X has shape {X.shape} "
            f"and Y has shape {Y.shape}."
        )

    X = np.array(X, dtype=np.float32)
    Y = np.array(Y, dtype=np.float32)
    Z = 1 - np.array(simd.cdist(X, Y, metric="cosine"))
    if isinstance(Z, float):
        return np.array([Z])
    return np.array(Z)


def _raise_missing_mmr_deps_error(parent_error: ModuleNotFoundError) -> None:
    import sys

    raise ModuleNotFoundError(
        f"Failed to compute maximal marginal relevance because the required "
        f"module '{parent_error.name}' is missing. You can install it by running: "
        f"'{sys.executable} -m pip install elasticsearch[vectorstore_mmr]'"
    ) from parent_error
