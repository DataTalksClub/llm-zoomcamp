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

import typing as t

from elastic_transport import ObjectApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class MlClient(NamespacedClient):

    @_rewrite_parameters()
    def clear_trained_model_deployment_cache(
        self,
        *,
        model_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Clear the cached results from a trained model deployment

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/clear-trained-model-deployment-cache.html>`_

        :param model_id: The unique identifier of the trained model.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = (
            f'/_ml/trained_models/{__path_parts["model_id"]}/deployment/cache/_clear'
        )
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.clear_trained_model_deployment_cache",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("allow_no_match", "force", "timeout"),
    )
    def close_job(
        self,
        *,
        job_id: str,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Closes one or more anomaly detection jobs. A job can be opened and closed multiple
        times throughout its lifecycle.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-close-job.html>`_

        :param job_id: Identifier for the anomaly detection job. It can be a job identifier,
            a group name, or a wildcard expression. You can close multiple anomaly detection
            jobs in a single API request by using a group name, a comma-separated list
            of jobs, or a wildcard expression. You can close all jobs by using `_all`
            or by specifying `*` as the job identifier.
        :param allow_no_match: Refer to the description for the `allow_no_match` query
            parameter.
        :param force: Refer to the descriptiion for the `force` query parameter.
        :param timeout: Refer to the description for the `timeout` query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_close'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_no_match is not None:
                __body["allow_no_match"] = allow_no_match
            if force is not None:
                __body["force"] = force
            if timeout is not None:
                __body["timeout"] = timeout
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.close_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_calendar(
        self,
        *,
        calendar_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a calendar.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-calendar.html>`_

        :param calendar_id: A string that uniquely identifies a calendar.
        """
        if calendar_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'calendar_id'")
        __path_parts: t.Dict[str, str] = {"calendar_id": _quote(calendar_id)}
        __path = f'/_ml/calendars/{__path_parts["calendar_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_calendar",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_calendar_event(
        self,
        *,
        calendar_id: str,
        event_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes scheduled events from a calendar.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-calendar-event.html>`_

        :param calendar_id: A string that uniquely identifies a calendar.
        :param event_id: Identifier for the scheduled event. You can obtain this identifier
            by using the get calendar events API.
        """
        if calendar_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'calendar_id'")
        if event_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'event_id'")
        __path_parts: t.Dict[str, str] = {
            "calendar_id": _quote(calendar_id),
            "event_id": _quote(event_id),
        }
        __path = f'/_ml/calendars/{__path_parts["calendar_id"]}/events/{__path_parts["event_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_calendar_event",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_calendar_job(
        self,
        *,
        calendar_id: str,
        job_id: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes anomaly detection jobs from a calendar.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-calendar-job.html>`_

        :param calendar_id: A string that uniquely identifies a calendar.
        :param job_id: An identifier for the anomaly detection jobs. It can be a job
            identifier, a group name, or a comma-separated list of jobs or groups.
        """
        if calendar_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'calendar_id'")
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {
            "calendar_id": _quote(calendar_id),
            "job_id": _quote(job_id),
        }
        __path = f'/_ml/calendars/{__path_parts["calendar_id"]}/jobs/{__path_parts["job_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_calendar_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_data_frame_analytics(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an existing data frame analytics job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job.
        :param force: If `true`, it deletes a job that is not stopped; this method is
            quicker than stopping and deleting the job.
        :param timeout: The time to wait for the job to be deleted.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force is not None:
            __query["force"] = force
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_datafeed(
        self,
        *,
        datafeed_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an existing datafeed.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-datafeed.html>`_

        :param datafeed_id: A numerical character string that uniquely identifies the
            datafeed. This identifier can contain lowercase alphanumeric characters (a-z
            and 0-9), hyphens, and underscores. It must start and end with alphanumeric
            characters.
        :param force: Use to forcefully delete a started datafeed; this method is quicker
            than stopping and deleting the datafeed.
        """
        if datafeed_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'datafeed_id'")
        __path_parts: t.Dict[str, str] = {"datafeed_id": _quote(datafeed_id)}
        __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force is not None:
            __query["force"] = force
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_datafeed",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("requests_per_second", "timeout"),
    )
    def delete_expired_data(
        self,
        *,
        job_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        requests_per_second: t.Optional[float] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes expired and unused machine learning data.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-expired-data.html>`_

        :param job_id: Identifier for an anomaly detection job. It can be a job identifier,
            a group name, or a wildcard expression.
        :param requests_per_second: The desired requests per second for the deletion
            processes. The default behavior is no throttling.
        :param timeout: How long can the underlying delete processes run until they are
            canceled.
        """
        __path_parts: t.Dict[str, str]
        if job_id not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id)}
            __path = f'/_ml/_delete_expired_data/{__path_parts["job_id"]}'
        else:
            __path_parts = {}
            __path = "/_ml/_delete_expired_data"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if requests_per_second is not None:
                __body["requests_per_second"] = requests_per_second
            if timeout is not None:
                __body["timeout"] = timeout
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.delete_expired_data",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_filter(
        self,
        *,
        filter_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a filter.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-filter.html>`_

        :param filter_id: A string that uniquely identifies a filter.
        """
        if filter_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'filter_id'")
        __path_parts: t.Dict[str, str] = {"filter_id": _quote(filter_id)}
        __path = f'/_ml/filters/{__path_parts["filter_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_filter",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_forecast(
        self,
        *,
        job_id: str,
        forecast_id: t.Optional[str] = None,
        allow_no_forecasts: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes forecasts from a machine learning job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-forecast.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param forecast_id: A comma-separated list of forecast identifiers. If you do
            not specify this optional parameter or if you specify `_all` or `*` the API
            deletes all forecasts from the job.
        :param allow_no_forecasts: Specifies whether an error occurs when there are no
            forecasts. In particular, if this parameter is set to `false` and there are
            no forecasts associated with the job, attempts to delete all forecasts return
            an error.
        :param timeout: Specifies the period of time to wait for the completion of the
            delete operation. When this period of time elapses, the API fails and returns
            an error.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str]
        if job_id not in SKIP_IN_PATH and forecast_id not in SKIP_IN_PATH:
            __path_parts = {
                "job_id": _quote(job_id),
                "forecast_id": _quote(forecast_id),
            }
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_forecast/{__path_parts["forecast_id"]}'
        elif job_id not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id)}
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_forecast'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        if allow_no_forecasts is not None:
            __query["allow_no_forecasts"] = allow_no_forecasts
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_forecast",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_job(
        self,
        *,
        job_id: str,
        delete_user_annotations: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        wait_for_completion: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an existing anomaly detection job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-job.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param delete_user_annotations: Specifies whether annotations that have been
            added by the user should be deleted along with any auto-generated annotations
            when the job is reset.
        :param force: Use to forcefully delete an opened job; this method is quicker
            than closing and deleting the job.
        :param wait_for_completion: Specifies whether the request should return immediately
            or wait until the job deletion completes.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if delete_user_annotations is not None:
            __query["delete_user_annotations"] = delete_user_annotations
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force is not None:
            __query["force"] = force
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_model_snapshot(
        self,
        *,
        job_id: str,
        snapshot_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an existing model snapshot.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-delete-snapshot.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param snapshot_id: Identifier for the model snapshot.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        if snapshot_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot_id'")
        __path_parts: t.Dict[str, str] = {
            "job_id": _quote(job_id),
            "snapshot_id": _quote(snapshot_id),
        }
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/model_snapshots/{__path_parts["snapshot_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_model_snapshot",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_trained_model(
        self,
        *,
        model_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes an existing trained inference model that is currently not referenced
        by an ingest pipeline.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-trained-models.html>`_

        :param model_id: The unique identifier of the trained model.
        :param force: Forcefully deletes a trained model that is referenced by ingest
            pipelines or has a started deployment.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force is not None:
            __query["force"] = force
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_trained_model",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def delete_trained_model_alias(
        self,
        *,
        model_id: str,
        model_alias: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a model alias that refers to the trained model

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/delete-trained-models-aliases.html>`_

        :param model_id: The trained model ID to which the model alias refers.
        :param model_alias: The model alias to delete.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        if model_alias in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_alias'")
        __path_parts: t.Dict[str, str] = {
            "model_id": _quote(model_id),
            "model_alias": _quote(model_alias),
        }
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/model_aliases/{__path_parts["model_alias"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.delete_trained_model_alias",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "analysis_config",
            "max_bucket_cardinality",
            "overall_cardinality",
        ),
    )
    def estimate_model_memory(
        self,
        *,
        analysis_config: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        max_bucket_cardinality: t.Optional[t.Mapping[str, int]] = None,
        overall_cardinality: t.Optional[t.Mapping[str, int]] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Estimates the model memory

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-apis.html>`_

        :param analysis_config: For a list of the properties that you can specify in
            the `analysis_config` component of the body of this API.
        :param max_bucket_cardinality: Estimates of the highest cardinality in a single
            bucket that is observed for influencer fields over the time period that the
            job analyzes data. To produce a good answer, values must be provided for
            all influencer fields. Providing values for fields that are not listed as
            `influencers` has no effect on the estimation.
        :param overall_cardinality: Estimates of the cardinality that is observed for
            fields over the whole time period that the job analyzes data. To produce
            a good answer, values must be provided for fields referenced in the `by_field_name`,
            `over_field_name` and `partition_field_name` of any detectors. Providing
            values for other fields has no effect on the estimation. It can be omitted
            from the request if no detectors have a `by_field_name`, `over_field_name`
            or `partition_field_name`.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ml/anomaly_detectors/_estimate_model_memory"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if analysis_config is not None:
                __body["analysis_config"] = analysis_config
            if max_bucket_cardinality is not None:
                __body["max_bucket_cardinality"] = max_bucket_cardinality
            if overall_cardinality is not None:
                __body["overall_cardinality"] = overall_cardinality
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.estimate_model_memory",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("evaluation", "index", "query"),
    )
    def evaluate_data_frame(
        self,
        *,
        evaluation: t.Optional[t.Mapping[str, t.Any]] = None,
        index: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Evaluates the data frame analytics for an annotated index.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/evaluate-dfanalytics.html>`_

        :param evaluation: Defines the type of evaluation you want to perform.
        :param index: Defines the `index` in which the evaluation will be performed.
        :param query: A query clause that retrieves a subset of data from the source
            index.
        """
        if evaluation is None and body is None:
            raise ValueError("Empty value passed for parameter 'evaluation'")
        if index is None and body is None:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ml/data_frame/_evaluate"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if evaluation is not None:
                __body["evaluation"] = evaluation
            if index is not None:
                __body["index"] = index
            if query is not None:
                __body["query"] = query
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.evaluate_data_frame",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "allow_lazy_start",
            "analysis",
            "analyzed_fields",
            "description",
            "dest",
            "max_num_threads",
            "model_memory_limit",
            "source",
        ),
    )
    def explain_data_frame_analytics(
        self,
        *,
        id: t.Optional[str] = None,
        allow_lazy_start: t.Optional[bool] = None,
        analysis: t.Optional[t.Mapping[str, t.Any]] = None,
        analyzed_fields: t.Optional[t.Mapping[str, t.Any]] = None,
        description: t.Optional[str] = None,
        dest: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        max_num_threads: t.Optional[int] = None,
        model_memory_limit: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        source: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Explains a data frame analytics config.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/explain-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job. This identifier can contain
            lowercase alphanumeric characters (a-z and 0-9), hyphens, and underscores.
            It must start and end with alphanumeric characters.
        :param allow_lazy_start: Specifies whether this job can start when there is insufficient
            machine learning node capacity for it to be immediately assigned to a node.
        :param analysis: The analysis configuration, which contains the information necessary
            to perform one of the following types of analysis: classification, outlier
            detection, or regression.
        :param analyzed_fields: Specify includes and/or excludes patterns to select which
            fields will be included in the analysis. The patterns specified in excludes
            are applied last, therefore excludes takes precedence. In other words, if
            the same field is specified in both includes and excludes, then the field
            will not be included in the analysis.
        :param description: A description of the job.
        :param dest: The destination configuration, consisting of index and optionally
            results_field (ml by default).
        :param max_num_threads: The maximum number of threads to be used by the analysis.
            Using more threads may decrease the time necessary to complete the analysis
            at the cost of using more CPU. Note that the process may use additional threads
            for operational functionality other than the analysis itself.
        :param model_memory_limit: The approximate maximum amount of memory resources
            that are permitted for analytical processing. If your `elasticsearch.yml`
            file contains an `xpack.ml.max_model_memory_limit` setting, an error occurs
            when you try to create data frame analytics jobs that have `model_memory_limit`
            values greater than that setting.
        :param source: The configuration of how to source the analysis data. It requires
            an index. Optionally, query and _source may be specified.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}/_explain'
        else:
            __path_parts = {}
            __path = "/_ml/data_frame/analytics/_explain"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_lazy_start is not None:
                __body["allow_lazy_start"] = allow_lazy_start
            if analysis is not None:
                __body["analysis"] = analysis
            if analyzed_fields is not None:
                __body["analyzed_fields"] = analyzed_fields
            if description is not None:
                __body["description"] = description
            if dest is not None:
                __body["dest"] = dest
            if max_num_threads is not None:
                __body["max_num_threads"] = max_num_threads
            if model_memory_limit is not None:
                __body["model_memory_limit"] = model_memory_limit
            if source is not None:
                __body["source"] = source
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.explain_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("advance_time", "calc_interim", "end", "skip_time", "start"),
    )
    def flush_job(
        self,
        *,
        job_id: str,
        advance_time: t.Optional[t.Union[str, t.Any]] = None,
        calc_interim: t.Optional[bool] = None,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        skip_time: t.Optional[t.Union[str, t.Any]] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Forces any buffered data to be processed by the job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-flush-job.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param advance_time: Refer to the description for the `advance_time` query parameter.
        :param calc_interim: Refer to the description for the `calc_interim` query parameter.
        :param end: Refer to the description for the `end` query parameter.
        :param skip_time: Refer to the description for the `skip_time` query parameter.
        :param start: Refer to the description for the `start` query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_flush'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if advance_time is not None:
                __body["advance_time"] = advance_time
            if calc_interim is not None:
                __body["calc_interim"] = calc_interim
            if end is not None:
                __body["end"] = end
            if skip_time is not None:
                __body["skip_time"] = skip_time
            if start is not None:
                __body["start"] = start
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.flush_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("duration", "expires_in", "max_model_memory"),
    )
    def forecast(
        self,
        *,
        job_id: str,
        duration: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        error_trace: t.Optional[bool] = None,
        expires_in: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        max_model_memory: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Predicts the future behavior of a time series by using its historical behavior.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-forecast.html>`_

        :param job_id: Identifier for the anomaly detection job. The job must be open
            when you create a forecast; otherwise, an error occurs.
        :param duration: Refer to the description for the `duration` query parameter.
        :param expires_in: Refer to the description for the `expires_in` query parameter.
        :param max_model_memory: Refer to the description for the `max_model_memory`
            query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_forecast'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if duration is not None:
                __body["duration"] = duration
            if expires_in is not None:
                __body["expires_in"] = expires_in
            if max_model_memory is not None:
                __body["max_model_memory"] = max_model_memory
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.forecast",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "anomaly_score",
            "desc",
            "end",
            "exclude_interim",
            "expand",
            "page",
            "sort",
            "start",
        ),
        parameter_aliases={"from": "from_"},
    )
    def get_buckets(
        self,
        *,
        job_id: str,
        timestamp: t.Optional[t.Union[str, t.Any]] = None,
        anomaly_score: t.Optional[float] = None,
        desc: t.Optional[bool] = None,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        exclude_interim: t.Optional[bool] = None,
        expand: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        page: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[str] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves anomaly detection job results for one or more buckets.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-bucket.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param timestamp: The timestamp of a single bucket result. If you do not specify
            this parameter, the API returns information about all buckets.
        :param anomaly_score: Refer to the description for the `anomaly_score` query
            parameter.
        :param desc: Refer to the description for the `desc` query parameter.
        :param end: Refer to the description for the `end` query parameter.
        :param exclude_interim: Refer to the description for the `exclude_interim` query
            parameter.
        :param expand: Refer to the description for the `expand` query parameter.
        :param from_: Skips the specified number of buckets.
        :param page:
        :param size: Specifies the maximum number of buckets to obtain.
        :param sort: Refer to the desription for the `sort` query parameter.
        :param start: Refer to the description for the `start` query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str]
        if job_id not in SKIP_IN_PATH and timestamp not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id), "timestamp": _quote(timestamp)}
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/results/buckets/{__path_parts["timestamp"]}'
        elif job_id not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id)}
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/results/buckets'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if not __body:
            if anomaly_score is not None:
                __body["anomaly_score"] = anomaly_score
            if desc is not None:
                __body["desc"] = desc
            if end is not None:
                __body["end"] = end
            if exclude_interim is not None:
                __body["exclude_interim"] = exclude_interim
            if expand is not None:
                __body["expand"] = expand
            if page is not None:
                __body["page"] = page
            if sort is not None:
                __body["sort"] = sort
            if start is not None:
                __body["start"] = start
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.get_buckets",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    def get_calendar_events(
        self,
        *,
        calendar_id: str,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        job_id: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves information about the scheduled events in calendars.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-calendar-event.html>`_

        :param calendar_id: A string that uniquely identifies a calendar. You can get
            information for multiple calendars by using a comma-separated list of ids
            or a wildcard expression. You can get information for all calendars by using
            `_all` or `*` or by omitting the calendar identifier.
        :param end: Specifies to get events with timestamps earlier than this time.
        :param from_: Skips the specified number of events.
        :param job_id: Specifies to get events for a specific anomaly detection job identifier
            or job group. It must be used with a calendar identifier of `_all` or `*`.
        :param size: Specifies the maximum number of events to obtain.
        :param start: Specifies to get events with timestamps after this time.
        """
        if calendar_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'calendar_id'")
        __path_parts: t.Dict[str, str] = {"calendar_id": _quote(calendar_id)}
        __path = f'/_ml/calendars/{__path_parts["calendar_id"]}/events'
        __query: t.Dict[str, t.Any] = {}
        if end is not None:
            __query["end"] = end
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if job_id is not None:
            __query["job_id"] = job_id
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if start is not None:
            __query["start"] = start
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_calendar_events",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("page",),
        parameter_aliases={"from": "from_"},
    )
    def get_calendars(
        self,
        *,
        calendar_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        page: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves configuration information for calendars.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-calendar.html>`_

        :param calendar_id: A string that uniquely identifies a calendar. You can get
            information for multiple calendars by using a comma-separated list of ids
            or a wildcard expression. You can get information for all calendars by using
            `_all` or `*` or by omitting the calendar identifier.
        :param from_: Skips the specified number of calendars. This parameter is supported
            only when you omit the calendar identifier.
        :param page: This object is supported only when you omit the calendar identifier.
        :param size: Specifies the maximum number of calendars to obtain. This parameter
            is supported only when you omit the calendar identifier.
        """
        __path_parts: t.Dict[str, str]
        if calendar_id not in SKIP_IN_PATH:
            __path_parts = {"calendar_id": _quote(calendar_id)}
            __path = f'/_ml/calendars/{__path_parts["calendar_id"]}'
        else:
            __path_parts = {}
            __path = "/_ml/calendars"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if not __body:
            if page is not None:
                __body["page"] = page
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.get_calendars",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("page",),
        parameter_aliases={"from": "from_"},
    )
    def get_categories(
        self,
        *,
        job_id: str,
        category_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        page: t.Optional[t.Mapping[str, t.Any]] = None,
        partition_field_value: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves anomaly detection job results for one or more categories.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-category.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param category_id: Identifier for the category, which is unique in the job.
            If you specify neither the category ID nor the partition_field_value, the
            API returns information about all categories. If you specify only the partition_field_value,
            it returns information about all categories for the specified partition.
        :param from_: Skips the specified number of categories.
        :param page: Configures pagination. This parameter has the `from` and `size`
            properties.
        :param partition_field_value: Only return categories for the specified partition.
        :param size: Specifies the maximum number of categories to obtain.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str]
        if job_id not in SKIP_IN_PATH and category_id not in SKIP_IN_PATH:
            __path_parts = {
                "job_id": _quote(job_id),
                "category_id": _quote(category_id),
            }
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/results/categories/{__path_parts["category_id"]}'
        elif job_id not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id)}
            __path = (
                f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/results/categories'
            )
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if partition_field_value is not None:
            __query["partition_field_value"] = partition_field_value
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if not __body:
            if page is not None:
                __body["page"] = page
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.get_categories",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    def get_data_frame_analytics(
        self,
        *,
        id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        exclude_generated: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves configuration information for data frame analytics jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job. If you do not specify
            this option, the API returns information for the first hundred data frame
            analytics jobs.
        :param allow_no_match: Specifies what to do when the request: 1. Contains wildcard
            expressions and there are no data frame analytics jobs that match. 2. Contains
            the `_all` string or no identifiers and there are no matches. 3. Contains
            wildcard expressions and there are only partial matches. The default value
            returns an empty data_frame_analytics array when there are no matches and
            the subset of results when there are partial matches. If this parameter is
            `false`, the request returns a 404 status code when there are no matches
            or only partial matches.
        :param exclude_generated: Indicates if certain fields should be removed from
            the configuration on retrieval. This allows the configuration to be in an
            acceptable format to be retrieved and then added to another cluster.
        :param from_: Skips the specified number of data frame analytics jobs.
        :param size: Specifies the maximum number of data frame analytics jobs to obtain.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}'
        else:
            __path_parts = {}
            __path = "/_ml/data_frame/analytics"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if exclude_generated is not None:
            __query["exclude_generated"] = exclude_generated
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    def get_data_frame_analytics_stats(
        self,
        *,
        id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        verbose: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves usage information for data frame analytics jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-dfanalytics-stats.html>`_

        :param id: Identifier for the data frame analytics job. If you do not specify
            this option, the API returns information for the first hundred data frame
            analytics jobs.
        :param allow_no_match: Specifies what to do when the request: 1. Contains wildcard
            expressions and there are no data frame analytics jobs that match. 2. Contains
            the `_all` string or no identifiers and there are no matches. 3. Contains
            wildcard expressions and there are only partial matches. The default value
            returns an empty data_frame_analytics array when there are no matches and
            the subset of results when there are partial matches. If this parameter is
            `false`, the request returns a 404 status code when there are no matches
            or only partial matches.
        :param from_: Skips the specified number of data frame analytics jobs.
        :param size: Specifies the maximum number of data frame analytics jobs to obtain.
        :param verbose: Defines whether the stats response should be verbose.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}/_stats'
        else:
            __path_parts = {}
            __path = "/_ml/data_frame/analytics/_stats"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if verbose is not None:
            __query["verbose"] = verbose
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_data_frame_analytics_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_datafeed_stats(
        self,
        *,
        datafeed_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves usage information for datafeeds.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-datafeed-stats.html>`_

        :param datafeed_id: Identifier for the datafeed. It can be a datafeed identifier
            or a wildcard expression. If you do not specify one of these options, the
            API returns information about all datafeeds.
        :param allow_no_match: Specifies what to do when the request: 1. Contains wildcard
            expressions and there are no datafeeds that match. 2. Contains the `_all`
            string or no identifiers and there are no matches. 3. Contains wildcard expressions
            and there are only partial matches. The default value is `true`, which returns
            an empty `datafeeds` array when there are no matches and the subset of results
            when there are partial matches. If this parameter is `false`, the request
            returns a `404` status code when there are no matches or only partial matches.
        """
        __path_parts: t.Dict[str, str]
        if datafeed_id not in SKIP_IN_PATH:
            __path_parts = {"datafeed_id": _quote(datafeed_id)}
            __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}/_stats'
        else:
            __path_parts = {}
            __path = "/_ml/datafeeds/_stats"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_datafeed_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_datafeeds(
        self,
        *,
        datafeed_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        exclude_generated: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves configuration information for datafeeds.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-datafeed.html>`_

        :param datafeed_id: Identifier for the datafeed. It can be a datafeed identifier
            or a wildcard expression. If you do not specify one of these options, the
            API returns information about all datafeeds.
        :param allow_no_match: Specifies what to do when the request: 1. Contains wildcard
            expressions and there are no datafeeds that match. 2. Contains the `_all`
            string or no identifiers and there are no matches. 3. Contains wildcard expressions
            and there are only partial matches. The default value is `true`, which returns
            an empty `datafeeds` array when there are no matches and the subset of results
            when there are partial matches. If this parameter is `false`, the request
            returns a `404` status code when there are no matches or only partial matches.
        :param exclude_generated: Indicates if certain fields should be removed from
            the configuration on retrieval. This allows the configuration to be in an
            acceptable format to be retrieved and then added to another cluster.
        """
        __path_parts: t.Dict[str, str]
        if datafeed_id not in SKIP_IN_PATH:
            __path_parts = {"datafeed_id": _quote(datafeed_id)}
            __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}'
        else:
            __path_parts = {}
            __path = "/_ml/datafeeds"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if exclude_generated is not None:
            __query["exclude_generated"] = exclude_generated
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_datafeeds",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    def get_filters(
        self,
        *,
        filter_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves filters.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-filter.html>`_

        :param filter_id: A string that uniquely identifies a filter.
        :param from_: Skips the specified number of filters.
        :param size: Specifies the maximum number of filters to obtain.
        """
        __path_parts: t.Dict[str, str]
        if filter_id not in SKIP_IN_PATH:
            __path_parts = {"filter_id": _quote(filter_id)}
            __path = f'/_ml/filters/{__path_parts["filter_id"]}'
        else:
            __path_parts = {}
            __path = "/_ml/filters"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_filters",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("page",),
        parameter_aliases={"from": "from_"},
    )
    def get_influencers(
        self,
        *,
        job_id: str,
        desc: t.Optional[bool] = None,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        exclude_interim: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        influencer_score: t.Optional[float] = None,
        page: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[str] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves anomaly detection job results for one or more influencers.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-influencer.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param desc: If true, the results are sorted in descending order.
        :param end: Returns influencers with timestamps earlier than this time. The default
            value means it is unset and results are not limited to specific timestamps.
        :param exclude_interim: If true, the output excludes interim results. By default,
            interim results are included.
        :param from_: Skips the specified number of influencers.
        :param influencer_score: Returns influencers with anomaly scores greater than
            or equal to this value.
        :param page: Configures pagination. This parameter has the `from` and `size`
            properties.
        :param size: Specifies the maximum number of influencers to obtain.
        :param sort: Specifies the sort field for the requested influencers. By default,
            the influencers are sorted by the `influencer_score` value.
        :param start: Returns influencers with timestamps after this time. The default
            value means it is unset and results are not limited to specific timestamps.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/results/influencers'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if desc is not None:
            __query["desc"] = desc
        if end is not None:
            __query["end"] = end
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if exclude_interim is not None:
            __query["exclude_interim"] = exclude_interim
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if influencer_score is not None:
            __query["influencer_score"] = influencer_score
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if sort is not None:
            __query["sort"] = sort
        if start is not None:
            __query["start"] = start
        if not __body:
            if page is not None:
                __body["page"] = page
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.get_influencers",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_job_stats(
        self,
        *,
        job_id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves usage information for anomaly detection jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-job-stats.html>`_

        :param job_id: Identifier for the anomaly detection job. It can be a job identifier,
            a group name, a comma-separated list of jobs, or a wildcard expression. If
            you do not specify one of these options, the API returns information for
            all anomaly detection jobs.
        :param allow_no_match: Specifies what to do when the request: 1. Contains wildcard
            expressions and there are no jobs that match. 2. Contains the _all string
            or no identifiers and there are no matches. 3. Contains wildcard expressions
            and there are only partial matches. If `true`, the API returns an empty `jobs`
            array when there are no matches and the subset of results when there are
            partial matches. If `false`, the API returns a `404` status code when there
            are no matches or only partial matches.
        """
        __path_parts: t.Dict[str, str]
        if job_id not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id)}
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_stats'
        else:
            __path_parts = {}
            __path = "/_ml/anomaly_detectors/_stats"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_job_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_jobs(
        self,
        *,
        job_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        exclude_generated: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves configuration information for anomaly detection jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-job.html>`_

        :param job_id: Identifier for the anomaly detection job. It can be a job identifier,
            a group name, or a wildcard expression. If you do not specify one of these
            options, the API returns information for all anomaly detection jobs.
        :param allow_no_match: Specifies what to do when the request: 1. Contains wildcard
            expressions and there are no jobs that match. 2. Contains the _all string
            or no identifiers and there are no matches. 3. Contains wildcard expressions
            and there are only partial matches. The default value is `true`, which returns
            an empty `jobs` array when there are no matches and the subset of results
            when there are partial matches. If this parameter is `false`, the request
            returns a `404` status code when there are no matches or only partial matches.
        :param exclude_generated: Indicates if certain fields should be removed from
            the configuration on retrieval. This allows the configuration to be in an
            acceptable format to be retrieved and then added to another cluster.
        """
        __path_parts: t.Dict[str, str]
        if job_id not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id)}
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}'
        else:
            __path_parts = {}
            __path = "/_ml/anomaly_detectors"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if exclude_generated is not None:
            __query["exclude_generated"] = exclude_generated
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_jobs",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_memory_stats(
        self,
        *,
        node_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns information on how ML is using memory.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-ml-memory.html>`_

        :param node_id: The names of particular nodes in the cluster to target. For example,
            `nodeId1,nodeId2` or `ml:true`
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        __path_parts: t.Dict[str, str]
        if node_id not in SKIP_IN_PATH:
            __path_parts = {"node_id": _quote(node_id)}
            __path = f'/_ml/memory/{__path_parts["node_id"]}/_stats'
        else:
            __path_parts = {}
            __path = "/_ml/memory/_stats"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_memory_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def get_model_snapshot_upgrade_stats(
        self,
        *,
        job_id: str,
        snapshot_id: str,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Gets stats for anomaly detection job model snapshot upgrades that are in progress.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-job-model-snapshot-upgrade-stats.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param snapshot_id: A numerical character string that uniquely identifies the
            model snapshot. You can get information for multiple snapshots by using a
            comma-separated list or a wildcard expression. You can get all snapshots
            by using `_all`, by specifying `*` as the snapshot ID, or by omitting the
            snapshot ID.
        :param allow_no_match: Specifies what to do when the request: - Contains wildcard
            expressions and there are no jobs that match. - Contains the _all string
            or no identifiers and there are no matches. - Contains wildcard expressions
            and there are only partial matches. The default value is true, which returns
            an empty jobs array when there are no matches and the subset of results when
            there are partial matches. If this parameter is false, the request returns
            a 404 status code when there are no matches or only partial matches.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        if snapshot_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot_id'")
        __path_parts: t.Dict[str, str] = {
            "job_id": _quote(job_id),
            "snapshot_id": _quote(snapshot_id),
        }
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/model_snapshots/{__path_parts["snapshot_id"]}/_upgrade/_stats'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_model_snapshot_upgrade_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("desc", "end", "page", "sort", "start"),
        parameter_aliases={"from": "from_"},
    )
    def get_model_snapshots(
        self,
        *,
        job_id: str,
        snapshot_id: t.Optional[str] = None,
        desc: t.Optional[bool] = None,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        page: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[str] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves information about model snapshots.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-snapshot.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param snapshot_id: A numerical character string that uniquely identifies the
            model snapshot. You can get information for multiple snapshots by using a
            comma-separated list or a wildcard expression. You can get all snapshots
            by using `_all`, by specifying `*` as the snapshot ID, or by omitting the
            snapshot ID.
        :param desc: Refer to the description for the `desc` query parameter.
        :param end: Refer to the description for the `end` query parameter.
        :param from_: Skips the specified number of snapshots.
        :param page:
        :param size: Specifies the maximum number of snapshots to obtain.
        :param sort: Refer to the description for the `sort` query parameter.
        :param start: Refer to the description for the `start` query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str]
        if job_id not in SKIP_IN_PATH and snapshot_id not in SKIP_IN_PATH:
            __path_parts = {
                "job_id": _quote(job_id),
                "snapshot_id": _quote(snapshot_id),
            }
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/model_snapshots/{__path_parts["snapshot_id"]}'
        elif job_id not in SKIP_IN_PATH:
            __path_parts = {"job_id": _quote(job_id)}
            __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/model_snapshots'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if not __body:
            if desc is not None:
                __body["desc"] = desc
            if end is not None:
                __body["end"] = end
            if page is not None:
                __body["page"] = page
            if sort is not None:
                __body["sort"] = sort
            if start is not None:
                __body["start"] = start
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.get_model_snapshots",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "allow_no_match",
            "bucket_span",
            "end",
            "exclude_interim",
            "overall_score",
            "start",
            "top_n",
        ),
    )
    def get_overall_buckets(
        self,
        *,
        job_id: str,
        allow_no_match: t.Optional[bool] = None,
        bucket_span: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        exclude_interim: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        overall_score: t.Optional[t.Union[float, str]] = None,
        pretty: t.Optional[bool] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        top_n: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves overall bucket results that summarize the bucket results of multiple
        anomaly detection jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-overall-buckets.html>`_

        :param job_id: Identifier for the anomaly detection job. It can be a job identifier,
            a group name, a comma-separated list of jobs or groups, or a wildcard expression.
            You can summarize the bucket results for all anomaly detection jobs by using
            `_all` or by specifying `*` as the `<job_id>`.
        :param allow_no_match: Refer to the description for the `allow_no_match` query
            parameter.
        :param bucket_span: Refer to the description for the `bucket_span` query parameter.
        :param end: Refer to the description for the `end` query parameter.
        :param exclude_interim: Refer to the description for the `exclude_interim` query
            parameter.
        :param overall_score: Refer to the description for the `overall_score` query
            parameter.
        :param start: Refer to the description for the `start` query parameter.
        :param top_n: Refer to the description for the `top_n` query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = (
            f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/results/overall_buckets'
        )
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_no_match is not None:
                __body["allow_no_match"] = allow_no_match
            if bucket_span is not None:
                __body["bucket_span"] = bucket_span
            if end is not None:
                __body["end"] = end
            if exclude_interim is not None:
                __body["exclude_interim"] = exclude_interim
            if overall_score is not None:
                __body["overall_score"] = overall_score
            if start is not None:
                __body["start"] = start
            if top_n is not None:
                __body["top_n"] = top_n
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.get_overall_buckets",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "desc",
            "end",
            "exclude_interim",
            "page",
            "record_score",
            "sort",
            "start",
        ),
        parameter_aliases={"from": "from_"},
    )
    def get_records(
        self,
        *,
        job_id: str,
        desc: t.Optional[bool] = None,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        exclude_interim: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        page: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        record_score: t.Optional[float] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[str] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves anomaly records for an anomaly detection job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-get-record.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param desc: Refer to the description for the `desc` query parameter.
        :param end: Refer to the description for the `end` query parameter.
        :param exclude_interim: Refer to the description for the `exclude_interim` query
            parameter.
        :param from_: Skips the specified number of records.
        :param page:
        :param record_score: Refer to the description for the `record_score` query parameter.
        :param size: Specifies the maximum number of records to obtain.
        :param sort: Refer to the description for the `sort` query parameter.
        :param start: Refer to the description for the `start` query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/results/records'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if not __body:
            if desc is not None:
                __body["desc"] = desc
            if end is not None:
                __body["end"] = end
            if exclude_interim is not None:
                __body["exclude_interim"] = exclude_interim
            if page is not None:
                __body["page"] = page
            if record_score is not None:
                __body["record_score"] = record_score
            if sort is not None:
                __body["sort"] = sort
            if start is not None:
                __body["start"] = start
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.get_records",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    def get_trained_models(
        self,
        *,
        model_id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        decompress_definition: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        exclude_generated: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        include: t.Optional[
            t.Union[
                "t.Literal['definition', 'definition_status', 'feature_importance_baseline', 'hyperparameters', 'total_feature_importance']",
                str,
            ]
        ] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        tags: t.Optional[str] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves configuration information for a trained inference model.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-trained-models.html>`_

        :param model_id: The unique identifier of the trained model.
        :param allow_no_match: Specifies what to do when the request: - Contains wildcard
            expressions and there are no models that match. - Contains the _all string
            or no identifiers and there are no matches. - Contains wildcard expressions
            and there are only partial matches. If true, it returns an empty array when
            there are no matches and the subset of results when there are partial matches.
        :param decompress_definition: Specifies whether the included model definition
            should be returned as a JSON map (true) or in a custom compressed format
            (false).
        :param exclude_generated: Indicates if certain fields should be removed from
            the configuration on retrieval. This allows the configuration to be in an
            acceptable format to be retrieved and then added to another cluster.
        :param from_: Skips the specified number of models.
        :param include: A comma delimited string of optional fields to include in the
            response body.
        :param size: Specifies the maximum number of models to obtain.
        :param tags: A comma delimited string of tags. A trained model can have many
            tags, or none. When supplied, only trained models that contain all the supplied
            tags are returned.
        """
        __path_parts: t.Dict[str, str]
        if model_id not in SKIP_IN_PATH:
            __path_parts = {"model_id": _quote(model_id)}
            __path = f'/_ml/trained_models/{__path_parts["model_id"]}'
        else:
            __path_parts = {}
            __path = "/_ml/trained_models"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if decompress_definition is not None:
            __query["decompress_definition"] = decompress_definition
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if exclude_generated is not None:
            __query["exclude_generated"] = exclude_generated
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if include is not None:
            __query["include"] = include
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if tags is not None:
            __query["tags"] = tags
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_trained_models",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    def get_trained_models_stats(
        self,
        *,
        model_id: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves usage information for trained inference models.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-trained-models-stats.html>`_

        :param model_id: The unique identifier of the trained model or a model alias.
            It can be a comma-separated list or a wildcard expression.
        :param allow_no_match: Specifies what to do when the request: - Contains wildcard
            expressions and there are no models that match. - Contains the _all string
            or no identifiers and there are no matches. - Contains wildcard expressions
            and there are only partial matches. If true, it returns an empty array when
            there are no matches and the subset of results when there are partial matches.
        :param from_: Skips the specified number of models.
        :param size: Specifies the maximum number of models to obtain.
        """
        __path_parts: t.Dict[str, str]
        if model_id not in SKIP_IN_PATH:
            __path_parts = {"model_id": _quote(model_id)}
            __path = f'/_ml/trained_models/{__path_parts["model_id"]}/_stats'
        else:
            __path_parts = {}
            __path = "/_ml/trained_models/_stats"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.get_trained_models_stats",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("docs", "inference_config"),
    )
    def infer_trained_model(
        self,
        *,
        model_id: str,
        docs: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        inference_config: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Evaluate a trained model.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/infer-trained-model.html>`_

        :param model_id: The unique identifier of the trained model.
        :param docs: An array of objects to pass to the model for inference. The objects
            should contain a fields matching your configured trained model input. Typically,
            for NLP models, the field name is `text_field`. Currently, for NLP models,
            only a single value is allowed.
        :param inference_config: The inference configuration updates to apply on the
            API call
        :param timeout: Controls the amount of time to wait for inference results.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        if docs is None and body is None:
            raise ValueError("Empty value passed for parameter 'docs'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/_infer'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if docs is not None:
                __body["docs"] = docs
            if inference_config is not None:
                __body["inference_config"] = inference_config
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.infer_trained_model",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def info(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns defaults and limits used by machine learning.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/get-ml-info.html>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ml/info"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.info",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("timeout",),
    )
    def open_job(
        self,
        *,
        job_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Opens one or more anomaly detection jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-open-job.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param timeout: Refer to the description for the `timeout` query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_open'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if timeout is not None:
                __body["timeout"] = timeout
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.open_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("events",),
    )
    def post_calendar_events(
        self,
        *,
        calendar_id: str,
        events: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Posts scheduled events in a calendar.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-post-calendar-event.html>`_

        :param calendar_id: A string that uniquely identifies a calendar.
        :param events: A list of one of more scheduled events. The event’s start and
            end times can be specified as integer milliseconds since the epoch or as
            a string in ISO 8601 format.
        """
        if calendar_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'calendar_id'")
        if events is None and body is None:
            raise ValueError("Empty value passed for parameter 'events'")
        __path_parts: t.Dict[str, str] = {"calendar_id": _quote(calendar_id)}
        __path = f'/_ml/calendars/{__path_parts["calendar_id"]}/events'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if events is not None:
                __body["events"] = events
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.post_calendar_events",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="data",
    )
    def post_data(
        self,
        *,
        job_id: str,
        data: t.Optional[t.Sequence[t.Any]] = None,
        body: t.Optional[t.Sequence[t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        reset_end: t.Optional[t.Union[str, t.Any]] = None,
        reset_start: t.Optional[t.Union[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Sends data to an anomaly detection job for analysis.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-post-data.html>`_

        :param job_id: Identifier for the anomaly detection job. The job must have a
            state of open to receive and process the data.
        :param data:
        :param reset_end: Specifies the end of the bucket resetting range.
        :param reset_start: Specifies the start of the bucket resetting range.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        if data is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'data' and 'body', one of them should be set."
            )
        elif data is not None and body is not None:
            raise ValueError("Cannot set both 'data' and 'body'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_data'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if reset_end is not None:
            __query["reset_end"] = reset_end
        if reset_start is not None:
            __query["reset_start"] = reset_start
        __body = data if data is not None else body
        __headers = {
            "accept": "application/json",
            "content-type": "application/x-ndjson",
        }
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.post_data",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("config",),
    )
    def preview_data_frame_analytics(
        self,
        *,
        id: t.Optional[str] = None,
        config: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Previews that will be analyzed given a data frame analytics config.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/preview-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job.
        :param config: A data frame analytics config as described in create data frame
            analytics jobs. Note that `id` and `dest` don’t need to be provided in the
            context of this API.
        """
        __path_parts: t.Dict[str, str]
        if id not in SKIP_IN_PATH:
            __path_parts = {"id": _quote(id)}
            __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}/_preview'
        else:
            __path_parts = {}
            __path = "/_ml/data_frame/analytics/_preview"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if config is not None:
                __body["config"] = config
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.preview_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("datafeed_config", "job_config"),
    )
    def preview_datafeed(
        self,
        *,
        datafeed_id: t.Optional[str] = None,
        datafeed_config: t.Optional[t.Mapping[str, t.Any]] = None,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        job_config: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Previews a datafeed.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-preview-datafeed.html>`_

        :param datafeed_id: A numerical character string that uniquely identifies the
            datafeed. This identifier can contain lowercase alphanumeric characters (a-z
            and 0-9), hyphens, and underscores. It must start and end with alphanumeric
            characters. NOTE: If you use this path parameter, you cannot provide datafeed
            or anomaly detection job configuration details in the request body.
        :param datafeed_config: The datafeed definition to preview.
        :param end: The end time when the datafeed preview should stop
        :param job_config: The configuration details for the anomaly detection job that
            is associated with the datafeed. If the `datafeed_config` object does not
            include a `job_id` that references an existing anomaly detection job, you
            must supply this `job_config` object. If you include both a `job_id` and
            a `job_config`, the latter information is used. You cannot specify a `job_config`
            object unless you also supply a `datafeed_config` object.
        :param start: The start time from where the datafeed preview should begin
        """
        __path_parts: t.Dict[str, str]
        if datafeed_id not in SKIP_IN_PATH:
            __path_parts = {"datafeed_id": _quote(datafeed_id)}
            __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}/_preview'
        else:
            __path_parts = {}
            __path = "/_ml/datafeeds/_preview"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if end is not None:
            __query["end"] = end
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if start is not None:
            __query["start"] = start
        if not __body:
            if datafeed_config is not None:
                __body["datafeed_config"] = datafeed_config
            if job_config is not None:
                __body["job_config"] = job_config
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.preview_datafeed",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("description", "job_ids"),
    )
    def put_calendar(
        self,
        *,
        calendar_id: str,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        job_ids: t.Optional[t.Sequence[str]] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Instantiates a calendar.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-put-calendar.html>`_

        :param calendar_id: A string that uniquely identifies a calendar.
        :param description: A description of the calendar.
        :param job_ids: An array of anomaly detection job identifiers.
        """
        if calendar_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'calendar_id'")
        __path_parts: t.Dict[str, str] = {"calendar_id": _quote(calendar_id)}
        __path = f'/_ml/calendars/{__path_parts["calendar_id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if description is not None:
                __body["description"] = description
            if job_ids is not None:
                __body["job_ids"] = job_ids
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_calendar",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def put_calendar_job(
        self,
        *,
        calendar_id: str,
        job_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Adds an anomaly detection job to a calendar.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-put-calendar-job.html>`_

        :param calendar_id: A string that uniquely identifies a calendar.
        :param job_id: An identifier for the anomaly detection jobs. It can be a job
            identifier, a group name, or a comma-separated list of jobs or groups.
        """
        if calendar_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'calendar_id'")
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {
            "calendar_id": _quote(calendar_id),
            "job_id": _quote(job_id),
        }
        __path = f'/_ml/calendars/{__path_parts["calendar_id"]}/jobs/{__path_parts["job_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.put_calendar_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "analysis",
            "dest",
            "source",
            "allow_lazy_start",
            "analyzed_fields",
            "description",
            "headers",
            "max_num_threads",
            "model_memory_limit",
            "version",
        ),
        ignore_deprecated_options={"headers"},
    )
    def put_data_frame_analytics(
        self,
        *,
        id: str,
        analysis: t.Optional[t.Mapping[str, t.Any]] = None,
        dest: t.Optional[t.Mapping[str, t.Any]] = None,
        source: t.Optional[t.Mapping[str, t.Any]] = None,
        allow_lazy_start: t.Optional[bool] = None,
        analyzed_fields: t.Optional[t.Mapping[str, t.Any]] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        headers: t.Optional[t.Mapping[str, t.Union[str, t.Sequence[str]]]] = None,
        human: t.Optional[bool] = None,
        max_num_threads: t.Optional[int] = None,
        model_memory_limit: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        version: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Instantiates a data frame analytics job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job. This identifier can contain
            lowercase alphanumeric characters (a-z and 0-9), hyphens, and underscores.
            It must start and end with alphanumeric characters.
        :param analysis: The analysis configuration, which contains the information necessary
            to perform one of the following types of analysis: classification, outlier
            detection, or regression.
        :param dest: The destination configuration.
        :param source: The configuration of how to source the analysis data.
        :param allow_lazy_start: Specifies whether this job can start when there is insufficient
            machine learning node capacity for it to be immediately assigned to a node.
            If set to `false` and a machine learning node with capacity to run the job
            cannot be immediately found, the API returns an error. If set to `true`,
            the API does not return an error; the job waits in the `starting` state until
            sufficient machine learning node capacity is available. This behavior is
            also affected by the cluster-wide `xpack.ml.max_lazy_ml_nodes` setting.
        :param analyzed_fields: Specifies `includes` and/or `excludes` patterns to select
            which fields will be included in the analysis. The patterns specified in
            `excludes` are applied last, therefore `excludes` takes precedence. In other
            words, if the same field is specified in both `includes` and `excludes`,
            then the field will not be included in the analysis. If `analyzed_fields`
            is not set, only the relevant fields will be included. For example, all the
            numeric fields for outlier detection. The supported fields vary for each
            type of analysis. Outlier detection requires numeric or `boolean` data to
            analyze. The algorithms don’t support missing values therefore fields that
            have data types other than numeric or boolean are ignored. Documents where
            included fields contain missing values, null values, or an array are also
            ignored. Therefore the `dest` index may contain documents that don’t have
            an outlier score. Regression supports fields that are numeric, `boolean`,
            `text`, `keyword`, and `ip` data types. It is also tolerant of missing values.
            Fields that are supported are included in the analysis, other fields are
            ignored. Documents where included fields contain an array with two or more
            values are also ignored. Documents in the `dest` index that don’t contain
            a results field are not included in the regression analysis. Classification
            supports fields that are numeric, `boolean`, `text`, `keyword`, and `ip`
            data types. It is also tolerant of missing values. Fields that are supported
            are included in the analysis, other fields are ignored. Documents where included
            fields contain an array with two or more values are also ignored. Documents
            in the `dest` index that don’t contain a results field are not included in
            the classification analysis. Classification analysis can be improved by mapping
            ordinal variable values to a single number. For example, in case of age ranges,
            you can model the values as `0-14 = 0`, `15-24 = 1`, `25-34 = 2`, and so
            on.
        :param description: A description of the job.
        :param headers:
        :param max_num_threads: The maximum number of threads to be used by the analysis.
            Using more threads may decrease the time necessary to complete the analysis
            at the cost of using more CPU. Note that the process may use additional threads
            for operational functionality other than the analysis itself.
        :param model_memory_limit: The approximate maximum amount of memory resources
            that are permitted for analytical processing. If your `elasticsearch.yml`
            file contains an `xpack.ml.max_model_memory_limit` setting, an error occurs
            when you try to create data frame analytics jobs that have `model_memory_limit`
            values greater than that setting.
        :param version:
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        if analysis is None and body is None:
            raise ValueError("Empty value passed for parameter 'analysis'")
        if dest is None and body is None:
            raise ValueError("Empty value passed for parameter 'dest'")
        if source is None and body is None:
            raise ValueError("Empty value passed for parameter 'source'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if analysis is not None:
                __body["analysis"] = analysis
            if dest is not None:
                __body["dest"] = dest
            if source is not None:
                __body["source"] = source
            if allow_lazy_start is not None:
                __body["allow_lazy_start"] = allow_lazy_start
            if analyzed_fields is not None:
                __body["analyzed_fields"] = analyzed_fields
            if description is not None:
                __body["description"] = description
            if headers is not None:
                __body["headers"] = headers
            if max_num_threads is not None:
                __body["max_num_threads"] = max_num_threads
            if model_memory_limit is not None:
                __body["model_memory_limit"] = model_memory_limit
            if version is not None:
                __body["version"] = version
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "aggregations",
            "chunking_config",
            "delayed_data_check_config",
            "frequency",
            "headers",
            "indexes",
            "indices",
            "indices_options",
            "job_id",
            "max_empty_searches",
            "query",
            "query_delay",
            "runtime_mappings",
            "script_fields",
            "scroll_size",
        ),
        ignore_deprecated_options={"headers"},
    )
    def put_datafeed(
        self,
        *,
        datafeed_id: str,
        aggregations: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        chunking_config: t.Optional[t.Mapping[str, t.Any]] = None,
        delayed_data_check_config: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        frequency: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        headers: t.Optional[t.Mapping[str, t.Union[str, t.Sequence[str]]]] = None,
        human: t.Optional[bool] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        indexes: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        indices: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        indices_options: t.Optional[t.Mapping[str, t.Any]] = None,
        job_id: t.Optional[str] = None,
        max_empty_searches: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        query_delay: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        runtime_mappings: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        script_fields: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        scroll_size: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Instantiates a datafeed.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-put-datafeed.html>`_

        :param datafeed_id: A numerical character string that uniquely identifies the
            datafeed. This identifier can contain lowercase alphanumeric characters (a-z
            and 0-9), hyphens, and underscores. It must start and end with alphanumeric
            characters.
        :param aggregations: If set, the datafeed performs aggregation searches. Support
            for aggregations is limited and should be used only with low cardinality
            data.
        :param allow_no_indices: If true, wildcard indices expressions that resolve into
            no concrete indices are ignored. This includes the `_all` string or when
            no indices are specified.
        :param chunking_config: Datafeeds might be required to search over long time
            periods, for several months or years. This search is split into time chunks
            in order to ensure the load on Elasticsearch is managed. Chunking configuration
            controls how the size of these time chunks are calculated; it is an advanced
            configuration option.
        :param delayed_data_check_config: Specifies whether the datafeed checks for missing
            data and the size of the window. The datafeed can optionally search over
            indices that have already been read in an effort to determine whether any
            data has subsequently been added to the index. If missing data is found,
            it is a good indication that the `query_delay` is set too low and the data
            is being indexed after the datafeed has passed that moment in time. This
            check runs only on real-time datafeeds.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values.
        :param frequency: The interval at which scheduled queries are made while the
            datafeed runs in real time. The default value is either the bucket span for
            short bucket spans, or, for longer bucket spans, a sensible fraction of the
            bucket span. When `frequency` is shorter than the bucket span, interim results
            for the last (partial) bucket are written then eventually overwritten by
            the full bucket results. If the datafeed uses aggregations, this value must
            be divisible by the interval of the date histogram aggregation.
        :param headers:
        :param ignore_throttled: If true, concrete, expanded, or aliased indices are
            ignored when frozen.
        :param ignore_unavailable: If true, unavailable indices (missing or closed) are
            ignored.
        :param indexes: An array of index names. Wildcards are supported. If any of the
            indices are in remote clusters, the machine learning nodes must have the
            `remote_cluster_client` role.
        :param indices: An array of index names. Wildcards are supported. If any of the
            indices are in remote clusters, the machine learning nodes must have the
            `remote_cluster_client` role.
        :param indices_options: Specifies index expansion options that are used during
            search
        :param job_id: Identifier for the anomaly detection job.
        :param max_empty_searches: If a real-time datafeed has never seen any data (including
            during any initial training period), it automatically stops and closes the
            associated job after this many real-time searches return no documents. In
            other words, it stops after `frequency` times `max_empty_searches` of real-time
            operation. If not set, a datafeed with no end time that sees no data remains
            started until it is explicitly stopped. By default, it is not set.
        :param query: The Elasticsearch query domain-specific language (DSL). This value
            corresponds to the query object in an Elasticsearch search POST body. All
            the options that are supported by Elasticsearch can be used, as this object
            is passed verbatim to Elasticsearch.
        :param query_delay: The number of seconds behind real time that data is queried.
            For example, if data from 10:04 a.m. might not be searchable in Elasticsearch
            until 10:06 a.m., set this property to 120 seconds. The default value is
            randomly selected between `60s` and `120s`. This randomness improves the
            query performance when there are multiple jobs running on the same node.
        :param runtime_mappings: Specifies runtime fields for the datafeed search.
        :param script_fields: Specifies scripts that evaluate custom expressions and
            returns script fields to the datafeed. The detector configuration objects
            in a job can contain functions that use these script fields.
        :param scroll_size: The size parameter that is used in Elasticsearch searches
            when the datafeed does not use aggregations. The maximum value is the value
            of `index.max_result_window`, which is 10,000 by default.
        """
        if datafeed_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'datafeed_id'")
        __path_parts: t.Dict[str, str] = {"datafeed_id": _quote(datafeed_id)}
        __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_throttled is not None:
            __query["ignore_throttled"] = ignore_throttled
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if aggregations is not None:
                __body["aggregations"] = aggregations
            if chunking_config is not None:
                __body["chunking_config"] = chunking_config
            if delayed_data_check_config is not None:
                __body["delayed_data_check_config"] = delayed_data_check_config
            if frequency is not None:
                __body["frequency"] = frequency
            if headers is not None:
                __body["headers"] = headers
            if indexes is not None:
                __body["indexes"] = indexes
            if indices is not None:
                __body["indices"] = indices
            if indices_options is not None:
                __body["indices_options"] = indices_options
            if job_id is not None:
                __body["job_id"] = job_id
            if max_empty_searches is not None:
                __body["max_empty_searches"] = max_empty_searches
            if query is not None:
                __body["query"] = query
            if query_delay is not None:
                __body["query_delay"] = query_delay
            if runtime_mappings is not None:
                __body["runtime_mappings"] = runtime_mappings
            if script_fields is not None:
                __body["script_fields"] = script_fields
            if scroll_size is not None:
                __body["scroll_size"] = scroll_size
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_datafeed",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("description", "items"),
    )
    def put_filter(
        self,
        *,
        filter_id: str,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        items: t.Optional[t.Sequence[str]] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Instantiates a filter.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-put-filter.html>`_

        :param filter_id: A string that uniquely identifies a filter.
        :param description: A description of the filter.
        :param items: The items of the filter. A wildcard `*` can be used at the beginning
            or the end of an item. Up to 10000 items are allowed in each filter.
        """
        if filter_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'filter_id'")
        __path_parts: t.Dict[str, str] = {"filter_id": _quote(filter_id)}
        __path = f'/_ml/filters/{__path_parts["filter_id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if description is not None:
                __body["description"] = description
            if items is not None:
                __body["items"] = items
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_filter",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "analysis_config",
            "data_description",
            "allow_lazy_open",
            "analysis_limits",
            "background_persist_interval",
            "custom_settings",
            "daily_model_snapshot_retention_after_days",
            "datafeed_config",
            "description",
            "groups",
            "model_plot_config",
            "model_snapshot_retention_days",
            "renormalization_window_days",
            "results_index_name",
            "results_retention_days",
        ),
    )
    def put_job(
        self,
        *,
        job_id: str,
        analysis_config: t.Optional[t.Mapping[str, t.Any]] = None,
        data_description: t.Optional[t.Mapping[str, t.Any]] = None,
        allow_lazy_open: t.Optional[bool] = None,
        analysis_limits: t.Optional[t.Mapping[str, t.Any]] = None,
        background_persist_interval: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        custom_settings: t.Optional[t.Any] = None,
        daily_model_snapshot_retention_after_days: t.Optional[int] = None,
        datafeed_config: t.Optional[t.Mapping[str, t.Any]] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        groups: t.Optional[t.Sequence[str]] = None,
        human: t.Optional[bool] = None,
        model_plot_config: t.Optional[t.Mapping[str, t.Any]] = None,
        model_snapshot_retention_days: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        renormalization_window_days: t.Optional[int] = None,
        results_index_name: t.Optional[str] = None,
        results_retention_days: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Instantiates an anomaly detection job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-put-job.html>`_

        :param job_id: The identifier for the anomaly detection job. This identifier
            can contain lowercase alphanumeric characters (a-z and 0-9), hyphens, and
            underscores. It must start and end with alphanumeric characters.
        :param analysis_config: Specifies how to analyze the data. After you create a
            job, you cannot change the analysis configuration; all the properties are
            informational.
        :param data_description: Defines the format of the input data when you send data
            to the job by using the post data API. Note that when configure a datafeed,
            these properties are automatically set. When data is received via the post
            data API, it is not stored in Elasticsearch. Only the results for anomaly
            detection are retained.
        :param allow_lazy_open: Advanced configuration option. Specifies whether this
            job can open when there is insufficient machine learning node capacity for
            it to be immediately assigned to a node. By default, if a machine learning
            node with capacity to run the job cannot immediately be found, the open anomaly
            detection jobs API returns an error. However, this is also subject to the
            cluster-wide `xpack.ml.max_lazy_ml_nodes` setting. If this option is set
            to true, the open anomaly detection jobs API does not return an error and
            the job waits in the opening state until sufficient machine learning node
            capacity is available.
        :param analysis_limits: Limits can be applied for the resources required to hold
            the mathematical models in memory. These limits are approximate and can be
            set per job. They do not control the memory used by other processes, for
            example the Elasticsearch Java processes.
        :param background_persist_interval: Advanced configuration option. The time between
            each periodic persistence of the model. The default value is a randomized
            value between 3 to 4 hours, which avoids all jobs persisting at exactly the
            same time. The smallest allowed value is 1 hour. For very large models (several
            GB), persistence could take 10-20 minutes, so do not set the `background_persist_interval`
            value too low.
        :param custom_settings: Advanced configuration option. Contains custom meta data
            about the job.
        :param daily_model_snapshot_retention_after_days: Advanced configuration option,
            which affects the automatic removal of old model snapshots for this job.
            It specifies a period of time (in days) after which only the first snapshot
            per day is retained. This period is relative to the timestamp of the most
            recent snapshot for this job. Valid values range from 0 to `model_snapshot_retention_days`.
        :param datafeed_config: Defines a datafeed for the anomaly detection job. If
            Elasticsearch security features are enabled, your datafeed remembers which
            roles the user who created it had at the time of creation and runs the query
            using those same roles. If you provide secondary authorization headers, those
            credentials are used instead.
        :param description: A description of the job.
        :param groups: A list of job groups. A job can belong to no groups or many.
        :param model_plot_config: This advanced configuration option stores model information
            along with the results. It provides a more detailed view into anomaly detection.
            If you enable model plot it can add considerable overhead to the performance
            of the system; it is not feasible for jobs with many entities. Model plot
            provides a simplified and indicative view of the model and its bounds. It
            does not display complex features such as multivariate correlations or multimodal
            data. As such, anomalies may occasionally be reported which cannot be seen
            in the model plot. Model plot config can be configured when the job is created
            or updated later. It must be disabled if performance issues are experienced.
        :param model_snapshot_retention_days: Advanced configuration option, which affects
            the automatic removal of old model snapshots for this job. It specifies the
            maximum period of time (in days) that snapshots are retained. This period
            is relative to the timestamp of the most recent snapshot for this job. By
            default, snapshots ten days older than the newest snapshot are deleted.
        :param renormalization_window_days: Advanced configuration option. The period
            over which adjustments to the score are applied, as new data is seen. The
            default value is the longer of 30 days or 100 bucket spans.
        :param results_index_name: A text string that affects the name of the machine
            learning results index. By default, the job generates an index named `.ml-anomalies-shared`.
        :param results_retention_days: Advanced configuration option. The period of time
            (in days) that results are retained. Age is calculated relative to the timestamp
            of the latest bucket result. If this property has a non-null value, once
            per day at 00:30 (server time), results that are the specified number of
            days older than the latest bucket result are deleted from Elasticsearch.
            The default value is null, which means all results are retained. Annotations
            generated by the system also count as results for retention purposes; they
            are deleted after the same number of days as results. Annotations added by
            users are retained forever.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        if analysis_config is None and body is None:
            raise ValueError("Empty value passed for parameter 'analysis_config'")
        if data_description is None and body is None:
            raise ValueError("Empty value passed for parameter 'data_description'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if analysis_config is not None:
                __body["analysis_config"] = analysis_config
            if data_description is not None:
                __body["data_description"] = data_description
            if allow_lazy_open is not None:
                __body["allow_lazy_open"] = allow_lazy_open
            if analysis_limits is not None:
                __body["analysis_limits"] = analysis_limits
            if background_persist_interval is not None:
                __body["background_persist_interval"] = background_persist_interval
            if custom_settings is not None:
                __body["custom_settings"] = custom_settings
            if daily_model_snapshot_retention_after_days is not None:
                __body["daily_model_snapshot_retention_after_days"] = (
                    daily_model_snapshot_retention_after_days
                )
            if datafeed_config is not None:
                __body["datafeed_config"] = datafeed_config
            if description is not None:
                __body["description"] = description
            if groups is not None:
                __body["groups"] = groups
            if model_plot_config is not None:
                __body["model_plot_config"] = model_plot_config
            if model_snapshot_retention_days is not None:
                __body["model_snapshot_retention_days"] = model_snapshot_retention_days
            if renormalization_window_days is not None:
                __body["renormalization_window_days"] = renormalization_window_days
            if results_index_name is not None:
                __body["results_index_name"] = results_index_name
            if results_retention_days is not None:
                __body["results_retention_days"] = results_retention_days
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "compressed_definition",
            "definition",
            "description",
            "inference_config",
            "input",
            "metadata",
            "model_size_bytes",
            "model_type",
            "platform_architecture",
            "prefix_strings",
            "tags",
        ),
    )
    def put_trained_model(
        self,
        *,
        model_id: str,
        compressed_definition: t.Optional[str] = None,
        defer_definition_decompression: t.Optional[bool] = None,
        definition: t.Optional[t.Mapping[str, t.Any]] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        inference_config: t.Optional[t.Mapping[str, t.Any]] = None,
        input: t.Optional[t.Mapping[str, t.Any]] = None,
        metadata: t.Optional[t.Any] = None,
        model_size_bytes: t.Optional[int] = None,
        model_type: t.Optional[
            t.Union["t.Literal['lang_ident', 'pytorch', 'tree_ensemble']", str]
        ] = None,
        platform_architecture: t.Optional[str] = None,
        prefix_strings: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        tags: t.Optional[t.Sequence[str]] = None,
        wait_for_completion: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates an inference trained model.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-trained-models.html>`_

        :param model_id: The unique identifier of the trained model.
        :param compressed_definition: The compressed (GZipped and Base64 encoded) inference
            definition of the model. If compressed_definition is specified, then definition
            cannot be specified.
        :param defer_definition_decompression: If set to `true` and a `compressed_definition`
            is provided, the request defers definition decompression and skips relevant
            validations.
        :param definition: The inference definition for the model. If definition is specified,
            then compressed_definition cannot be specified.
        :param description: A human-readable description of the inference trained model.
        :param inference_config: The default configuration for inference. This can be
            either a regression or classification configuration. It must match the underlying
            definition.trained_model's target_type. For pre-packaged models such as ELSER
            the config is not required.
        :param input: The input field names for the model definition.
        :param metadata: An object map that contains metadata about the model.
        :param model_size_bytes: The estimated memory usage in bytes to keep the trained
            model in memory. This property is supported only if defer_definition_decompression
            is true or the model definition is not supplied.
        :param model_type: The model type.
        :param platform_architecture: The platform architecture (if applicable) of the
            trained mode. If the model only works on one platform, because it is heavily
            optimized for a particular processor architecture and OS combination, then
            this field specifies which. The format of the string must match the platform
            identifiers used by Elasticsearch, so one of, `linux-x86_64`, `linux-aarch64`,
            `darwin-x86_64`, `darwin-aarch64`, or `windows-x86_64`. For portable models
            (those that work independent of processor architecture or OS features), leave
            this field unset.
        :param prefix_strings: Optional prefix strings applied at inference
        :param tags: An array of tags to organize the model.
        :param wait_for_completion: Whether to wait for all child operations (e.g. model
            download) to complete.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if defer_definition_decompression is not None:
            __query["defer_definition_decompression"] = defer_definition_decompression
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        if not __body:
            if compressed_definition is not None:
                __body["compressed_definition"] = compressed_definition
            if definition is not None:
                __body["definition"] = definition
            if description is not None:
                __body["description"] = description
            if inference_config is not None:
                __body["inference_config"] = inference_config
            if input is not None:
                __body["input"] = input
            if metadata is not None:
                __body["metadata"] = metadata
            if model_size_bytes is not None:
                __body["model_size_bytes"] = model_size_bytes
            if model_type is not None:
                __body["model_type"] = model_type
            if platform_architecture is not None:
                __body["platform_architecture"] = platform_architecture
            if prefix_strings is not None:
                __body["prefix_strings"] = prefix_strings
            if tags is not None:
                __body["tags"] = tags
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_trained_model",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def put_trained_model_alias(
        self,
        *,
        model_id: str,
        model_alias: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        reassign: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a new model alias (or reassigns an existing one) to refer to the trained
        model

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-trained-models-aliases.html>`_

        :param model_id: The identifier for the trained model that the alias refers to.
        :param model_alias: The alias to create or update. This value cannot end in numbers.
        :param reassign: Specifies whether the alias gets reassigned to the specified
            trained model if it is already assigned to a different model. If the alias
            is already assigned and this parameter is false, the API returns an error.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        if model_alias in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_alias'")
        __path_parts: t.Dict[str, str] = {
            "model_id": _quote(model_id),
            "model_alias": _quote(model_alias),
        }
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/model_aliases/{__path_parts["model_alias"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if reassign is not None:
            __query["reassign"] = reassign
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.put_trained_model_alias",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("definition", "total_definition_length", "total_parts"),
    )
    def put_trained_model_definition_part(
        self,
        *,
        model_id: str,
        part: int,
        definition: t.Optional[str] = None,
        total_definition_length: t.Optional[int] = None,
        total_parts: t.Optional[int] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates part of a trained model definition

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-trained-model-definition-part.html>`_

        :param model_id: The unique identifier of the trained model.
        :param part: The definition part number. When the definition is loaded for inference
            the definition parts are streamed in the order of their part number. The
            first part must be `0` and the final part must be `total_parts - 1`.
        :param definition: The definition part for the model. Must be a base64 encoded
            string.
        :param total_definition_length: The total uncompressed definition length in bytes.
            Not base64 encoded.
        :param total_parts: The total number of parts that will be uploaded. Must be
            greater than 0.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        if part in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'part'")
        if definition is None and body is None:
            raise ValueError("Empty value passed for parameter 'definition'")
        if total_definition_length is None and body is None:
            raise ValueError(
                "Empty value passed for parameter 'total_definition_length'"
            )
        if total_parts is None and body is None:
            raise ValueError("Empty value passed for parameter 'total_parts'")
        __path_parts: t.Dict[str, str] = {
            "model_id": _quote(model_id),
            "part": _quote(part),
        }
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/definition/{__path_parts["part"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if definition is not None:
                __body["definition"] = definition
            if total_definition_length is not None:
                __body["total_definition_length"] = total_definition_length
            if total_parts is not None:
                __body["total_parts"] = total_parts
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_trained_model_definition_part",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("vocabulary", "merges", "scores"),
    )
    def put_trained_model_vocabulary(
        self,
        *,
        model_id: str,
        vocabulary: t.Optional[t.Sequence[str]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        merges: t.Optional[t.Sequence[str]] = None,
        pretty: t.Optional[bool] = None,
        scores: t.Optional[t.Sequence[float]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates a trained model vocabulary

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/put-trained-model-vocabulary.html>`_

        :param model_id: The unique identifier of the trained model.
        :param vocabulary: The model vocabulary, which must not be empty.
        :param merges: The optional model merges if required by the tokenizer.
        :param scores: The optional vocabulary value scores if required by the tokenizer.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        if vocabulary is None and body is None:
            raise ValueError("Empty value passed for parameter 'vocabulary'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/vocabulary'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if vocabulary is not None:
                __body["vocabulary"] = vocabulary
            if merges is not None:
                __body["merges"] = merges
            if scores is not None:
                __body["scores"] = scores
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.put_trained_model_vocabulary",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def reset_job(
        self,
        *,
        job_id: str,
        delete_user_annotations: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        wait_for_completion: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Resets an existing anomaly detection job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-reset-job.html>`_

        :param job_id: The ID of the job to reset.
        :param delete_user_annotations: Specifies whether annotations that have been
            added by the user should be deleted along with any auto-generated annotations
            when the job is reset.
        :param wait_for_completion: Should this request wait until the operation has
            completed before returning.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_reset'
        __query: t.Dict[str, t.Any] = {}
        if delete_user_annotations is not None:
            __query["delete_user_annotations"] = delete_user_annotations
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.reset_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("delete_intervening_results",),
    )
    def revert_model_snapshot(
        self,
        *,
        job_id: str,
        snapshot_id: str,
        delete_intervening_results: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Reverts to a specific snapshot.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-revert-snapshot.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param snapshot_id: You can specify `empty` as the <snapshot_id>. Reverting to
            the empty snapshot means the anomaly detection job starts learning a new
            model from scratch when it is started.
        :param delete_intervening_results: Refer to the description for the `delete_intervening_results`
            query parameter.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        if snapshot_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot_id'")
        __path_parts: t.Dict[str, str] = {
            "job_id": _quote(job_id),
            "snapshot_id": _quote(snapshot_id),
        }
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/model_snapshots/{__path_parts["snapshot_id"]}/_revert'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if delete_intervening_results is not None:
                __body["delete_intervening_results"] = delete_intervening_results
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.revert_model_snapshot",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def set_upgrade_mode(
        self,
        *,
        enabled: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Sets a cluster wide upgrade_mode setting that prepares machine learning indices
        for an upgrade.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-set-upgrade-mode.html>`_

        :param enabled: When `true`, it enables `upgrade_mode` which temporarily halts
            all job and datafeed tasks and prohibits new job and datafeed tasks from
            starting.
        :param timeout: The time to wait for the request to be completed.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ml/set_upgrade_mode"
        __query: t.Dict[str, t.Any] = {}
        if enabled is not None:
            __query["enabled"] = enabled
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.set_upgrade_mode",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def start_data_frame_analytics(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Starts a data frame analytics job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/start-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job. This identifier can contain
            lowercase alphanumeric characters (a-z and 0-9), hyphens, and underscores.
            It must start and end with alphanumeric characters.
        :param timeout: Controls the amount of time to wait until the data frame analytics
            job starts.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}/_start'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.start_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("end", "start", "timeout"),
    )
    def start_datafeed(
        self,
        *,
        datafeed_id: str,
        end: t.Optional[t.Union[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        start: t.Optional[t.Union[str, t.Any]] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Starts one or more datafeeds.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-start-datafeed.html>`_

        :param datafeed_id: A numerical character string that uniquely identifies the
            datafeed. This identifier can contain lowercase alphanumeric characters (a-z
            and 0-9), hyphens, and underscores. It must start and end with alphanumeric
            characters.
        :param end: Refer to the description for the `end` query parameter.
        :param start: Refer to the description for the `start` query parameter.
        :param timeout: Refer to the description for the `timeout` query parameter.
        """
        if datafeed_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'datafeed_id'")
        __path_parts: t.Dict[str, str] = {"datafeed_id": _quote(datafeed_id)}
        __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}/_start'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if end is not None:
                __body["end"] = end
            if start is not None:
                __body["start"] = start
            if timeout is not None:
                __body["timeout"] = timeout
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.start_datafeed",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def start_trained_model_deployment(
        self,
        *,
        model_id: str,
        cache_size: t.Optional[t.Union[int, str]] = None,
        deployment_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        number_of_allocations: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        priority: t.Optional[t.Union["t.Literal['low', 'normal']", str]] = None,
        queue_capacity: t.Optional[int] = None,
        threads_per_allocation: t.Optional[int] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        wait_for: t.Optional[
            t.Union["t.Literal['fully_allocated', 'started', 'starting']", str]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Start a trained model deployment.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/start-trained-model-deployment.html>`_

        :param model_id: The unique identifier of the trained model. Currently, only
            PyTorch models are supported.
        :param cache_size: The inference cache size (in memory outside the JVM heap)
            per node for the model. The default value is the same size as the `model_size_bytes`.
            To disable the cache, `0b` can be provided.
        :param deployment_id: A unique identifier for the deployment of the model.
        :param number_of_allocations: The number of model allocations on each node where
            the model is deployed. All allocations on a node share the same copy of the
            model in memory but use a separate set of threads to evaluate the model.
            Increasing this value generally increases the throughput. If this setting
            is greater than the number of hardware threads it will automatically be changed
            to a value less than the number of hardware threads.
        :param priority: The deployment priority.
        :param queue_capacity: Specifies the number of inference requests that are allowed
            in the queue. After the number of requests exceeds this value, new requests
            are rejected with a 429 error.
        :param threads_per_allocation: Sets the number of threads used by each model
            allocation during inference. This generally increases the inference speed.
            The inference process is a compute-bound process; any number greater than
            the number of available hardware threads on the machine does not increase
            the inference speed. If this setting is greater than the number of hardware
            threads it will automatically be changed to a value less than the number
            of hardware threads.
        :param timeout: Specifies the amount of time to wait for the model to deploy.
        :param wait_for: Specifies the allocation status to wait for before returning.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/deployment/_start'
        __query: t.Dict[str, t.Any] = {}
        if cache_size is not None:
            __query["cache_size"] = cache_size
        if deployment_id is not None:
            __query["deployment_id"] = deployment_id
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if number_of_allocations is not None:
            __query["number_of_allocations"] = number_of_allocations
        if pretty is not None:
            __query["pretty"] = pretty
        if priority is not None:
            __query["priority"] = priority
        if queue_capacity is not None:
            __query["queue_capacity"] = queue_capacity
        if threads_per_allocation is not None:
            __query["threads_per_allocation"] = threads_per_allocation
        if timeout is not None:
            __query["timeout"] = timeout
        if wait_for is not None:
            __query["wait_for"] = wait_for
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.start_trained_model_deployment",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def stop_data_frame_analytics(
        self,
        *,
        id: str,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Stops one or more data frame analytics jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/stop-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job. This identifier can contain
            lowercase alphanumeric characters (a-z and 0-9), hyphens, and underscores.
            It must start and end with alphanumeric characters.
        :param allow_no_match: Specifies what to do when the request: 1. Contains wildcard
            expressions and there are no data frame analytics jobs that match. 2. Contains
            the _all string or no identifiers and there are no matches. 3. Contains wildcard
            expressions and there are only partial matches. The default value is true,
            which returns an empty data_frame_analytics array when there are no matches
            and the subset of results when there are partial matches. If this parameter
            is false, the request returns a 404 status code when there are no matches
            or only partial matches.
        :param force: If true, the data frame analytics job is stopped forcefully.
        :param timeout: Controls the amount of time to wait until the data frame analytics
            job stops. Defaults to 20 seconds.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}/_stop'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force is not None:
            __query["force"] = force
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.stop_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("allow_no_match", "force", "timeout"),
    )
    def stop_datafeed(
        self,
        *,
        datafeed_id: str,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Stops one or more datafeeds.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-stop-datafeed.html>`_

        :param datafeed_id: Identifier for the datafeed. You can stop multiple datafeeds
            in a single API request by using a comma-separated list of datafeeds or a
            wildcard expression. You can close all datafeeds by using `_all` or by specifying
            `*` as the identifier.
        :param allow_no_match: Refer to the description for the `allow_no_match` query
            parameter.
        :param force: Refer to the description for the `force` query parameter.
        :param timeout: Refer to the description for the `timeout` query parameter.
        """
        if datafeed_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'datafeed_id'")
        __path_parts: t.Dict[str, str] = {"datafeed_id": _quote(datafeed_id)}
        __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}/_stop'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_no_match is not None:
                __body["allow_no_match"] = allow_no_match
            if force is not None:
                __body["force"] = force
            if timeout is not None:
                __body["timeout"] = timeout
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.stop_datafeed",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def stop_trained_model_deployment(
        self,
        *,
        model_id: str,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Stop a trained model deployment.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/stop-trained-model-deployment.html>`_

        :param model_id: The unique identifier of the trained model.
        :param allow_no_match: Specifies what to do when the request: contains wildcard
            expressions and there are no deployments that match; contains the `_all`
            string or no identifiers and there are no matches; or contains wildcard expressions
            and there are only partial matches. By default, it returns an empty array
            when there are no matches and the subset of results when there are partial
            matches. If `false`, the request returns a 404 status code when there are
            no matches or only partial matches.
        :param force: Forcefully stops the deployment, even if it is used by ingest pipelines.
            You can't use these pipelines until you restart the model deployment.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/deployment/_stop'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force is not None:
            __query["force"] = force
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.stop_trained_model_deployment",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "allow_lazy_start",
            "description",
            "max_num_threads",
            "model_memory_limit",
        ),
    )
    def update_data_frame_analytics(
        self,
        *,
        id: str,
        allow_lazy_start: t.Optional[bool] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        max_num_threads: t.Optional[int] = None,
        model_memory_limit: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates certain properties of a data frame analytics job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/update-dfanalytics.html>`_

        :param id: Identifier for the data frame analytics job. This identifier can contain
            lowercase alphanumeric characters (a-z and 0-9), hyphens, and underscores.
            It must start and end with alphanumeric characters.
        :param allow_lazy_start: Specifies whether this job can start when there is insufficient
            machine learning node capacity for it to be immediately assigned to a node.
        :param description: A description of the job.
        :param max_num_threads: The maximum number of threads to be used by the analysis.
            Using more threads may decrease the time necessary to complete the analysis
            at the cost of using more CPU. Note that the process may use additional threads
            for operational functionality other than the analysis itself.
        :param model_memory_limit: The approximate maximum amount of memory resources
            that are permitted for analytical processing. If your `elasticsearch.yml`
            file contains an `xpack.ml.max_model_memory_limit` setting, an error occurs
            when you try to create data frame analytics jobs that have `model_memory_limit`
            values greater than that setting.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_ml/data_frame/analytics/{__path_parts["id"]}/_update'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_lazy_start is not None:
                __body["allow_lazy_start"] = allow_lazy_start
            if description is not None:
                __body["description"] = description
            if max_num_threads is not None:
                __body["max_num_threads"] = max_num_threads
            if model_memory_limit is not None:
                __body["model_memory_limit"] = model_memory_limit
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.update_data_frame_analytics",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "aggregations",
            "chunking_config",
            "delayed_data_check_config",
            "frequency",
            "indexes",
            "indices",
            "indices_options",
            "job_id",
            "max_empty_searches",
            "query",
            "query_delay",
            "runtime_mappings",
            "script_fields",
            "scroll_size",
        ),
    )
    def update_datafeed(
        self,
        *,
        datafeed_id: str,
        aggregations: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        chunking_config: t.Optional[t.Mapping[str, t.Any]] = None,
        delayed_data_check_config: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str]
                ],
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        frequency: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        human: t.Optional[bool] = None,
        ignore_throttled: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        indexes: t.Optional[t.Sequence[str]] = None,
        indices: t.Optional[t.Sequence[str]] = None,
        indices_options: t.Optional[t.Mapping[str, t.Any]] = None,
        job_id: t.Optional[str] = None,
        max_empty_searches: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        query_delay: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        runtime_mappings: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        script_fields: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        scroll_size: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates certain properties of a datafeed.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-update-datafeed.html>`_

        :param datafeed_id: A numerical character string that uniquely identifies the
            datafeed. This identifier can contain lowercase alphanumeric characters (a-z
            and 0-9), hyphens, and underscores. It must start and end with alphanumeric
            characters.
        :param aggregations: If set, the datafeed performs aggregation searches. Support
            for aggregations is limited and should be used only with low cardinality
            data.
        :param allow_no_indices: If `true`, wildcard indices expressions that resolve
            into no concrete indices are ignored. This includes the `_all` string or
            when no indices are specified.
        :param chunking_config: Datafeeds might search over long time periods, for several
            months or years. This search is split into time chunks in order to ensure
            the load on Elasticsearch is managed. Chunking configuration controls how
            the size of these time chunks are calculated; it is an advanced configuration
            option.
        :param delayed_data_check_config: Specifies whether the datafeed checks for missing
            data and the size of the window. The datafeed can optionally search over
            indices that have already been read in an effort to determine whether any
            data has subsequently been added to the index. If missing data is found,
            it is a good indication that the `query_delay` is set too low and the data
            is being indexed after the datafeed has passed that moment in time. This
            check runs only on real-time datafeeds.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values. Valid
            values are: * `all`: Match any data stream or index, including hidden ones.
            * `closed`: Match closed, non-hidden indices. Also matches any non-hidden
            data stream. Data streams cannot be closed. * `hidden`: Match hidden data
            streams and hidden indices. Must be combined with `open`, `closed`, or both.
            * `none`: Wildcard patterns are not accepted. * `open`: Match open, non-hidden
            indices. Also matches any non-hidden data stream.
        :param frequency: The interval at which scheduled queries are made while the
            datafeed runs in real time. The default value is either the bucket span for
            short bucket spans, or, for longer bucket spans, a sensible fraction of the
            bucket span. When `frequency` is shorter than the bucket span, interim results
            for the last (partial) bucket are written then eventually overwritten by
            the full bucket results. If the datafeed uses aggregations, this value must
            be divisible by the interval of the date histogram aggregation.
        :param ignore_throttled: If `true`, concrete, expanded or aliased indices are
            ignored when frozen.
        :param ignore_unavailable: If `true`, unavailable indices (missing or closed)
            are ignored.
        :param indexes: An array of index names. Wildcards are supported. If any of the
            indices are in remote clusters, the machine learning nodes must have the
            `remote_cluster_client` role.
        :param indices: An array of index names. Wildcards are supported. If any of the
            indices are in remote clusters, the machine learning nodes must have the
            `remote_cluster_client` role.
        :param indices_options: Specifies index expansion options that are used during
            search.
        :param job_id:
        :param max_empty_searches: If a real-time datafeed has never seen any data (including
            during any initial training period), it automatically stops and closes the
            associated job after this many real-time searches return no documents. In
            other words, it stops after `frequency` times `max_empty_searches` of real-time
            operation. If not set, a datafeed with no end time that sees no data remains
            started until it is explicitly stopped. By default, it is not set.
        :param query: The Elasticsearch query domain-specific language (DSL). This value
            corresponds to the query object in an Elasticsearch search POST body. All
            the options that are supported by Elasticsearch can be used, as this object
            is passed verbatim to Elasticsearch. Note that if you change the query, the
            analyzed data is also changed. Therefore, the time required to learn might
            be long and the understandability of the results is unpredictable. If you
            want to make significant changes to the source data, it is recommended that
            you clone the job and datafeed and make the amendments in the clone. Let
            both run in parallel and close one when you are satisfied with the results
            of the job.
        :param query_delay: The number of seconds behind real time that data is queried.
            For example, if data from 10:04 a.m. might not be searchable in Elasticsearch
            until 10:06 a.m., set this property to 120 seconds. The default value is
            randomly selected between `60s` and `120s`. This randomness improves the
            query performance when there are multiple jobs running on the same node.
        :param runtime_mappings: Specifies runtime fields for the datafeed search.
        :param script_fields: Specifies scripts that evaluate custom expressions and
            returns script fields to the datafeed. The detector configuration objects
            in a job can contain functions that use these script fields.
        :param scroll_size: The size parameter that is used in Elasticsearch searches
            when the datafeed does not use aggregations. The maximum value is the value
            of `index.max_result_window`.
        """
        if datafeed_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'datafeed_id'")
        __path_parts: t.Dict[str, str] = {"datafeed_id": _quote(datafeed_id)}
        __path = f'/_ml/datafeeds/{__path_parts["datafeed_id"]}/_update'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_throttled is not None:
            __query["ignore_throttled"] = ignore_throttled
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if aggregations is not None:
                __body["aggregations"] = aggregations
            if chunking_config is not None:
                __body["chunking_config"] = chunking_config
            if delayed_data_check_config is not None:
                __body["delayed_data_check_config"] = delayed_data_check_config
            if frequency is not None:
                __body["frequency"] = frequency
            if indexes is not None:
                __body["indexes"] = indexes
            if indices is not None:
                __body["indices"] = indices
            if indices_options is not None:
                __body["indices_options"] = indices_options
            if job_id is not None:
                __body["job_id"] = job_id
            if max_empty_searches is not None:
                __body["max_empty_searches"] = max_empty_searches
            if query is not None:
                __body["query"] = query
            if query_delay is not None:
                __body["query_delay"] = query_delay
            if runtime_mappings is not None:
                __body["runtime_mappings"] = runtime_mappings
            if script_fields is not None:
                __body["script_fields"] = script_fields
            if scroll_size is not None:
                __body["scroll_size"] = scroll_size
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.update_datafeed",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("add_items", "description", "remove_items"),
    )
    def update_filter(
        self,
        *,
        filter_id: str,
        add_items: t.Optional[t.Sequence[str]] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        remove_items: t.Optional[t.Sequence[str]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates the description of a filter, adds items, or removes items.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-update-filter.html>`_

        :param filter_id: A string that uniquely identifies a filter.
        :param add_items: The items to add to the filter.
        :param description: A description for the filter.
        :param remove_items: The items to remove from the filter.
        """
        if filter_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'filter_id'")
        __path_parts: t.Dict[str, str] = {"filter_id": _quote(filter_id)}
        __path = f'/_ml/filters/{__path_parts["filter_id"]}/_update'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if add_items is not None:
                __body["add_items"] = add_items
            if description is not None:
                __body["description"] = description
            if remove_items is not None:
                __body["remove_items"] = remove_items
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.update_filter",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "allow_lazy_open",
            "analysis_limits",
            "background_persist_interval",
            "categorization_filters",
            "custom_settings",
            "daily_model_snapshot_retention_after_days",
            "description",
            "detectors",
            "groups",
            "model_plot_config",
            "model_prune_window",
            "model_snapshot_retention_days",
            "per_partition_categorization",
            "renormalization_window_days",
            "results_retention_days",
        ),
    )
    def update_job(
        self,
        *,
        job_id: str,
        allow_lazy_open: t.Optional[bool] = None,
        analysis_limits: t.Optional[t.Mapping[str, t.Any]] = None,
        background_persist_interval: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        categorization_filters: t.Optional[t.Sequence[str]] = None,
        custom_settings: t.Optional[t.Mapping[str, t.Any]] = None,
        daily_model_snapshot_retention_after_days: t.Optional[int] = None,
        description: t.Optional[str] = None,
        detectors: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        groups: t.Optional[t.Sequence[str]] = None,
        human: t.Optional[bool] = None,
        model_plot_config: t.Optional[t.Mapping[str, t.Any]] = None,
        model_prune_window: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        model_snapshot_retention_days: t.Optional[int] = None,
        per_partition_categorization: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        renormalization_window_days: t.Optional[int] = None,
        results_retention_days: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates certain properties of an anomaly detection job.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-update-job.html>`_

        :param job_id: Identifier for the job.
        :param allow_lazy_open: Advanced configuration option. Specifies whether this
            job can open when there is insufficient machine learning node capacity for
            it to be immediately assigned to a node. If `false` and a machine learning
            node with capacity to run the job cannot immediately be found, the open anomaly
            detection jobs API returns an error. However, this is also subject to the
            cluster-wide `xpack.ml.max_lazy_ml_nodes` setting. If this option is set
            to `true`, the open anomaly detection jobs API does not return an error and
            the job waits in the opening state until sufficient machine learning node
            capacity is available.
        :param analysis_limits:
        :param background_persist_interval: Advanced configuration option. The time between
            each periodic persistence of the model. The default value is a randomized
            value between 3 to 4 hours, which avoids all jobs persisting at exactly the
            same time. The smallest allowed value is 1 hour. For very large models (several
            GB), persistence could take 10-20 minutes, so do not set the value too low.
            If the job is open when you make the update, you must stop the datafeed,
            close the job, then reopen the job and restart the datafeed for the changes
            to take effect.
        :param categorization_filters:
        :param custom_settings: Advanced configuration option. Contains custom meta data
            about the job. For example, it can contain custom URL information as shown
            in Adding custom URLs to machine learning results.
        :param daily_model_snapshot_retention_after_days: Advanced configuration option,
            which affects the automatic removal of old model snapshots for this job.
            It specifies a period of time (in days) after which only the first snapshot
            per day is retained. This period is relative to the timestamp of the most
            recent snapshot for this job. Valid values range from 0 to `model_snapshot_retention_days`.
            For jobs created before version 7.8.0, the default value matches `model_snapshot_retention_days`.
        :param description: A description of the job.
        :param detectors: An array of detector update objects.
        :param groups: A list of job groups. A job can belong to no groups or many.
        :param model_plot_config:
        :param model_prune_window:
        :param model_snapshot_retention_days: Advanced configuration option, which affects
            the automatic removal of old model snapshots for this job. It specifies the
            maximum period of time (in days) that snapshots are retained. This period
            is relative to the timestamp of the most recent snapshot for this job.
        :param per_partition_categorization: Settings related to how categorization interacts
            with partition fields.
        :param renormalization_window_days: Advanced configuration option. The period
            over which adjustments to the score are applied, as new data is seen.
        :param results_retention_days: Advanced configuration option. The period of time
            (in days) that results are retained. Age is calculated relative to the timestamp
            of the latest bucket result. If this property has a non-null value, once
            per day at 00:30 (server time), results that are the specified number of
            days older than the latest bucket result are deleted from Elasticsearch.
            The default value is null, which means all results are retained.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        __path_parts: t.Dict[str, str] = {"job_id": _quote(job_id)}
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/_update'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_lazy_open is not None:
                __body["allow_lazy_open"] = allow_lazy_open
            if analysis_limits is not None:
                __body["analysis_limits"] = analysis_limits
            if background_persist_interval is not None:
                __body["background_persist_interval"] = background_persist_interval
            if categorization_filters is not None:
                __body["categorization_filters"] = categorization_filters
            if custom_settings is not None:
                __body["custom_settings"] = custom_settings
            if daily_model_snapshot_retention_after_days is not None:
                __body["daily_model_snapshot_retention_after_days"] = (
                    daily_model_snapshot_retention_after_days
                )
            if description is not None:
                __body["description"] = description
            if detectors is not None:
                __body["detectors"] = detectors
            if groups is not None:
                __body["groups"] = groups
            if model_plot_config is not None:
                __body["model_plot_config"] = model_plot_config
            if model_prune_window is not None:
                __body["model_prune_window"] = model_prune_window
            if model_snapshot_retention_days is not None:
                __body["model_snapshot_retention_days"] = model_snapshot_retention_days
            if per_partition_categorization is not None:
                __body["per_partition_categorization"] = per_partition_categorization
            if renormalization_window_days is not None:
                __body["renormalization_window_days"] = renormalization_window_days
            if results_retention_days is not None:
                __body["results_retention_days"] = results_retention_days
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.update_job",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("description", "retain"),
    )
    def update_model_snapshot(
        self,
        *,
        job_id: str,
        snapshot_id: str,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        retain: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates certain properties of a snapshot.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-update-snapshot.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param snapshot_id: Identifier for the model snapshot.
        :param description: A description of the model snapshot.
        :param retain: If `true`, this snapshot will not be deleted during automatic
            cleanup of snapshots older than `model_snapshot_retention_days`. However,
            this snapshot will be deleted when the job is deleted.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        if snapshot_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot_id'")
        __path_parts: t.Dict[str, str] = {
            "job_id": _quote(job_id),
            "snapshot_id": _quote(snapshot_id),
        }
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/model_snapshots/{__path_parts["snapshot_id"]}/_update'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if description is not None:
                __body["description"] = description
            if retain is not None:
                __body["retain"] = retain
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.update_model_snapshot",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("number_of_allocations",),
    )
    def update_trained_model_deployment(
        self,
        *,
        model_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        number_of_allocations: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates certain properties of trained model deployment.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/update-trained-model-deployment.html>`_

        :param model_id: The unique identifier of the trained model. Currently, only
            PyTorch models are supported.
        :param number_of_allocations: The number of model allocations on each node where
            the model is deployed. All allocations on a node share the same copy of the
            model in memory but use a separate set of threads to evaluate the model.
            Increasing this value generally increases the throughput. If this setting
            is greater than the number of hardware threads it will automatically be changed
            to a value less than the number of hardware threads.
        """
        if model_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'model_id'")
        __path_parts: t.Dict[str, str] = {"model_id": _quote(model_id)}
        __path = f'/_ml/trained_models/{__path_parts["model_id"]}/deployment/_update'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if number_of_allocations is not None:
                __body["number_of_allocations"] = number_of_allocations
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.update_trained_model_deployment",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    def upgrade_job_snapshot(
        self,
        *,
        job_id: str,
        snapshot_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        wait_for_completion: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Upgrades a given job snapshot to the current major version.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/ml-upgrade-job-model-snapshot.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param snapshot_id: A numerical character string that uniquely identifies the
            model snapshot.
        :param timeout: Controls the time to wait for the request to complete.
        :param wait_for_completion: When true, the API won’t respond until the upgrade
            is complete. Otherwise, it responds as soon as the upgrade task is assigned
            to a node.
        """
        if job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'job_id'")
        if snapshot_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'snapshot_id'")
        __path_parts: t.Dict[str, str] = {
            "job_id": _quote(job_id),
            "snapshot_id": _quote(snapshot_id),
        }
        __path = f'/_ml/anomaly_detectors/{__path_parts["job_id"]}/model_snapshots/{__path_parts["snapshot_id"]}/_upgrade'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        if wait_for_completion is not None:
            __query["wait_for_completion"] = wait_for_completion
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="ml.upgrade_job_snapshot",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "analysis_config",
            "analysis_limits",
            "data_description",
            "description",
            "job_id",
            "model_plot",
            "model_snapshot_id",
            "model_snapshot_retention_days",
            "results_index_name",
        ),
    )
    def validate(
        self,
        *,
        analysis_config: t.Optional[t.Mapping[str, t.Any]] = None,
        analysis_limits: t.Optional[t.Mapping[str, t.Any]] = None,
        data_description: t.Optional[t.Mapping[str, t.Any]] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        job_id: t.Optional[str] = None,
        model_plot: t.Optional[t.Mapping[str, t.Any]] = None,
        model_snapshot_id: t.Optional[str] = None,
        model_snapshot_retention_days: t.Optional[int] = None,
        pretty: t.Optional[bool] = None,
        results_index_name: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Validates an anomaly detection job.

        `<https://www.elastic.co/guide/en/machine-learning/8.14/ml-jobs.html>`_

        :param analysis_config:
        :param analysis_limits:
        :param data_description:
        :param description:
        :param job_id:
        :param model_plot:
        :param model_snapshot_id:
        :param model_snapshot_retention_days:
        :param results_index_name:
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ml/anomaly_detectors/_validate"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if analysis_config is not None:
                __body["analysis_config"] = analysis_config
            if analysis_limits is not None:
                __body["analysis_limits"] = analysis_limits
            if data_description is not None:
                __body["data_description"] = data_description
            if description is not None:
                __body["description"] = description
            if job_id is not None:
                __body["job_id"] = job_id
            if model_plot is not None:
                __body["model_plot"] = model_plot
            if model_snapshot_id is not None:
                __body["model_snapshot_id"] = model_snapshot_id
            if model_snapshot_retention_days is not None:
                __body["model_snapshot_retention_days"] = model_snapshot_retention_days
            if results_index_name is not None:
                __body["results_index_name"] = results_index_name
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.validate",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="detector",
    )
    def validate_detector(
        self,
        *,
        detector: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Validates an anomaly detection detector.

        `<https://www.elastic.co/guide/en/machine-learning/8.14/ml-jobs.html>`_

        :param detector:
        """
        if detector is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'detector' and 'body', one of them should be set."
            )
        elif detector is not None and body is not None:
            raise ValueError("Cannot set both 'detector' and 'body'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_ml/anomaly_detectors/_validate/detector"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __body = detector if detector is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="ml.validate_detector",
            path_parts=__path_parts,
        )
