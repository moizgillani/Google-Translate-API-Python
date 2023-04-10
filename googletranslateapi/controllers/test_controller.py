# -*- coding: utf-8 -*-

"""
googletranslateapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from googletranslateapi.api_helper import APIHelper
from googletranslateapi.configuration import Server
from googletranslateapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from googletranslateapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or


class TestController(BaseController):

    """A Controller to access Endpoints in the googletranslateapi API."""
    def __init__(self, config):
        super(TestController, self).__init__(config)

    def languages(self):
        """Does a GET request to /languages.

        Returns a list of supported languages for translation.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/languages')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.dynamic_deserialize)
        ).execute()

    def detect(self,
               q,
               content_type):
        """Does a POST request to /detect.

        Detects the language of text within a request.

        Args:
            q (string): The input text upon which to perform language
                detection.
            content_type (string): defining content type as
                x-www-form-urlencoded

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/detect')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('q')
                        .value(q))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.dynamic_deserialize)
        ).execute()

    def translate(self,
                  q,
                  target):
        """Does a POST request to /.

        Translates input text, returning translated text

        Args:
            q (string): The input text to translate
            target (string): target language to translate the text to

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('q')
                        .value(q))
            .form_param(Parameter()
                        .key('target')
                        .value(target))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.dynamic_deserialize)
        ).execute()
