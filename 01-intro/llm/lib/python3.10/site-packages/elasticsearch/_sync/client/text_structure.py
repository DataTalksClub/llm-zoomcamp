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
from .utils import _rewrite_parameters


class TextStructureClient(NamespacedClient):

    @_rewrite_parameters(
        body_name="text_files",
    )
    def find_structure(
        self,
        *,
        text_files: t.Optional[t.Sequence[t.Any]] = None,
        body: t.Optional[t.Sequence[t.Any]] = None,
        charset: t.Optional[str] = None,
        column_names: t.Optional[str] = None,
        delimiter: t.Optional[str] = None,
        ecs_compatibility: t.Optional[str] = None,
        explain: t.Optional[bool] = None,
        format: t.Optional[str] = None,
        grok_pattern: t.Optional[str] = None,
        has_header_row: t.Optional[bool] = None,
        line_merge_size_limit: t.Optional[int] = None,
        lines_to_sample: t.Optional[int] = None,
        quote: t.Optional[str] = None,
        should_trim_fields: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        timestamp_field: t.Optional[str] = None,
        timestamp_format: t.Optional[str] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Finds the structure of a text file. The text file must contain data that is suitable
        to be ingested into Elasticsearch.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/find-structure.html>`_

        :param text_files:
        :param charset: The text’s character set. It must be a character set that is
            supported by the JVM that Elasticsearch uses. For example, UTF-8, UTF-16LE,
            windows-1252, or EUC-JP. If this parameter is not specified, the structure
            finder chooses an appropriate character set.
        :param column_names: If you have set format to delimited, you can specify the
            column names in a comma-separated list. If this parameter is not specified,
            the structure finder uses the column names from the header row of the text.
            If the text does not have a header role, columns are named "column1", "column2",
            "column3", etc.
        :param delimiter: If you have set format to delimited, you can specify the character
            used to delimit the values in each row. Only a single character is supported;
            the delimiter cannot have multiple characters. By default, the API considers
            the following possibilities: comma, tab, semi-colon, and pipe (|). In this
            default scenario, all rows must have the same number of fields for the delimited
            format to be detected. If you specify a delimiter, up to 10% of the rows
            can have a different number of columns than the first row.
        :param ecs_compatibility: The mode of compatibility with ECS compliant Grok patterns
            (disabled or v1, default: disabled).
        :param explain: If this parameter is set to true, the response includes a field
            named explanation, which is an array of strings that indicate how the structure
            finder produced its result.
        :param format: The high level structure of the text. Valid values are ndjson,
            xml, delimited, and semi_structured_text. By default, the API chooses the
            format. In this default scenario, all rows must have the same number of fields
            for a delimited format to be detected. If the format is set to delimited
            and the delimiter is not set, however, the API tolerates up to 5% of rows
            that have a different number of columns than the first row.
        :param grok_pattern: If you have set format to semi_structured_text, you can
            specify a Grok pattern that is used to extract fields from every message
            in the text. The name of the timestamp field in the Grok pattern must match
            what is specified in the timestamp_field parameter. If that parameter is
            not specified, the name of the timestamp field in the Grok pattern must match
            "timestamp". If grok_pattern is not specified, the structure finder creates
            a Grok pattern.
        :param has_header_row: If you have set format to delimited, you can use this
            parameter to indicate whether the column names are in the first row of the
            text. If this parameter is not specified, the structure finder guesses based
            on the similarity of the first row of the text to other rows.
        :param line_merge_size_limit: The maximum number of characters in a message when
            lines are merged to form messages while analyzing semi-structured text. If
            you have extremely long messages you may need to increase this, but be aware
            that this may lead to very long processing times if the way to group lines
            into messages is misdetected.
        :param lines_to_sample: The number of lines to include in the structural analysis,
            starting from the beginning of the text. The minimum is 2; If the value of
            this parameter is greater than the number of lines in the text, the analysis
            proceeds (as long as there are at least two lines in the text) for all of
            the lines.
        :param quote: If you have set format to delimited, you can specify the character
            used to quote the values in each row if they contain newlines or the delimiter
            character. Only a single character is supported. If this parameter is not
            specified, the default value is a double quote ("). If your delimited text
            format does not use quoting, a workaround is to set this argument to a character
            that does not appear anywhere in the sample.
        :param should_trim_fields: If you have set format to delimited, you can specify
            whether values between delimiters should have whitespace trimmed from them.
            If this parameter is not specified and the delimiter is pipe (|), the default
            value is true. Otherwise, the default value is false.
        :param timeout: Sets the maximum amount of time that the structure analysis make
            take. If the analysis is still running when the timeout expires then it will
            be aborted.
        :param timestamp_field: Optional parameter to specify the timestamp field in
            the file
        :param timestamp_format: The Java time format of the timestamp field in the text.
        """
        if text_files is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'text_files' and 'body', one of them should be set."
            )
        elif text_files is not None and body is not None:
            raise ValueError("Cannot set both 'text_files' and 'body'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_text_structure/find_structure"
        __query: t.Dict[str, t.Any] = {}
        if charset is not None:
            __query["charset"] = charset
        if column_names is not None:
            __query["column_names"] = column_names
        if delimiter is not None:
            __query["delimiter"] = delimiter
        if ecs_compatibility is not None:
            __query["ecs_compatibility"] = ecs_compatibility
        if explain is not None:
            __query["explain"] = explain
        if format is not None:
            __query["format"] = format
        if grok_pattern is not None:
            __query["grok_pattern"] = grok_pattern
        if has_header_row is not None:
            __query["has_header_row"] = has_header_row
        if line_merge_size_limit is not None:
            __query["line_merge_size_limit"] = line_merge_size_limit
        if lines_to_sample is not None:
            __query["lines_to_sample"] = lines_to_sample
        if quote is not None:
            __query["quote"] = quote
        if should_trim_fields is not None:
            __query["should_trim_fields"] = should_trim_fields
        if timeout is not None:
            __query["timeout"] = timeout
        if timestamp_field is not None:
            __query["timestamp_field"] = timestamp_field
        if timestamp_format is not None:
            __query["timestamp_format"] = timestamp_format
        __body = text_files if text_files is not None else body
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
            endpoint_id="text_structure.find_structure",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("grok_pattern", "text"),
    )
    def test_grok_pattern(
        self,
        *,
        grok_pattern: t.Optional[str] = None,
        text: t.Optional[t.Sequence[str]] = None,
        ecs_compatibility: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Tests a Grok pattern on some text.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/8.14/test-grok-pattern.html>`_

        :param grok_pattern: Grok pattern to run on the text.
        :param text: Lines of text to run the Grok pattern on.
        :param ecs_compatibility: The mode of compatibility with ECS compliant Grok patterns
            (disabled or v1, default: disabled).
        """
        if grok_pattern is None and body is None:
            raise ValueError("Empty value passed for parameter 'grok_pattern'")
        if text is None and body is None:
            raise ValueError("Empty value passed for parameter 'text'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_text_structure/test_grok_pattern"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if ecs_compatibility is not None:
            __query["ecs_compatibility"] = ecs_compatibility
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if grok_pattern is not None:
                __body["grok_pattern"] = grok_pattern
            if text is not None:
                __body["text"] = text
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="text_structure.test_grok_pattern",
            path_parts=__path_parts,
        )
