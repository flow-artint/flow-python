# -*- coding: utf-8 -*-

from flowai.rest.app_base     import AppBase
from flowai.rest.response     import Response
from flowai.constants.model   import Model
from flowai.constants.url     import URL
from flowai.rest.app_base     import AppBase

import requests
from os.path import join


class HttpClient(object):
    """Executes all the requests to be made to the server.
    """
    def __init__(self, api_key: str = None):
        # Assertions
        assert api_key != None, "Please insert your api_key."
        assert AppBase.is_valid_api_key(api_key), f"Invalid api_key. Please copy your api_key from {join(URL.BASE_URL, URL.DASHBOARD)}"
        
        self.__api_key = api_key

    def execute_request(
        self,
        input_url: str = None,
        model_name: str = None
    ) -> dict:
        # Assertions
        
        # None checks
        assert input_url != None, "Please insert your input_url."
        assert model_name != None, "Please insert your model_name."
        # Validation checks
        assert URL.is_valid(input_url), f"Entered input_url ({input_url}) argument is not valid. Please recheck it."
        assert Model.is_valid(self.__api_key, model_name), f"Entered model_name ({model_name}) argument is not valid. Please recheck it."

        def create_data(input_url: str, model_name: str) -> dict:
            """Create data to send to the server.
            """
            return {
                'data':     input_url,
                'api_key':  self.__api_key,
                'api_name': model_name
            }
        data = create_data(input_url, model_name)
        # Execute request
        call_url = join(URL.BASE_URL, URL.INFER)
        response = requests.post(call_url, json=data)
        # Extract useful data from response
        response = Response.clean(response)
        return response