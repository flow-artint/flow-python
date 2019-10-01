# -*- coding: utf-8 -*-

from flowai.constants.url     import URL
from flowai.rest.http_client  import HttpClient

from os.path import join


class Predictor(object):
    """Makes and returns the prediction to client.
    """

    def __init__(self, api_key: str = None):
        # initializations
        self.__http_client = HttpClient(api_key=api_key)

    def predict(
        self,
        input_url: str = None,
        model_name: str = None
    ) -> dict:
        # Execute request to get response
        response = self.__http_client.execute_request(input_url, model_name)
        # NOTE: Response is already cleaned by HttpClient.
        # So, simply return the response.
        return response