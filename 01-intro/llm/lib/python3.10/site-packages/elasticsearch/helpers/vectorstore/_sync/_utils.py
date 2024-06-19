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

from elasticsearch import BadRequestError, Elasticsearch, NotFoundError


def model_must_be_deployed(client: Elasticsearch, model_id: str) -> None:
    """
    :raises [NotFoundError]: if the model is neither downloaded nor deployed.
    :raises [ConflictError]: if the model is downloaded but not yet deployed.
    """
    doc = {"text_field": f"test if the model '{model_id}' is deployed"}
    try:
        client.ml.infer_trained_model(model_id=model_id, docs=[doc])
    except BadRequestError:
        # The model is deployed but expects a different input field name.
        pass


def model_is_deployed(client: Elasticsearch, model_id: str) -> bool:
    try:
        model_must_be_deployed(client, model_id)
        return True
    except NotFoundError:
        return False
