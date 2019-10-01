# -*- coding: utf-8 -*-

from flowai.constants.url import URL
from flowai.constants.model import Model

import requests
import json
from os.path import join

class AppBase(object):

    def __init__(self, model_name):
        pass

    def predict_by_url(self):
        pass

    def is_valid_api_key(api_key: str = None):
        # Make a validation check on server
        call_url = join(URL.BASE_URL, URL.CHECK_API_KEY)
        response = requests.post(call_url, json={"api_key": api_key})
        # Get into dictionary
        response_dict = json.loads(response.text)
        # Get success response value
        success = response_dict["success"]
        # Return validity status
        return True if success else False