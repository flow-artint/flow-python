# -*- coding: utf-8 -*-

from flowai.constants.url import URL

import requests
import json
from os.path import join

class Model(object):

    #####################
    # Indivisual models #
    #####################
    
    # Vision
    FACE_DETECTION = 'face-detection'
    # TODO: Coming soon!
    
    # Natural Language Processing
    # TODO: Coming soon!

    # Audio
    # TODO: Coming soon!

    ######################
    # Categorized models #
    ######################
    
    __VISION_MODELS: list = [
        FACE_DETECTION
    ]
    __NLP_MODELS: list = [
        # TODO: Coming soon!
    ]
    __AUDIO_MODELS: list = [
        # TODO: Coming soon!
    ]
    AVAILABLE_MODELS: list = [
        *_Model__VISION_MODELS,
        *_Model__NLP_MODELS,
        *_Model__AUDIO_MODELS,
    ]

    def __init__(self):
        pass

    def is_valid(api_key: str = None, model_name: str = None):
        
        model_is_available = Model.is_available(model_name)
        assert model_is_available, f"Entered model_name ({model_name}) is not available. Please import and use models in Model class: `from flow import Model`."

        # Now it's confirmed that model_name is available.
        call_url = join(URL.BASE_URL, URL.GET_MODEL_NAMES)
        response = requests.post(call_url, json={"api_key": api_key})
        response_dict = json.loads(response.text)

        data        = response_dict["data"]
        ready_apis  = []
        if data != {}:
            # Get the activated model names.
            ready_apis = data["ready_apis"]
            for idx, ready_api in enumerate(ready_apis):
                ready_apis[idx] = ready_api.lower().replace(' ', '-')
            # Compare ready_apis with entered model_name.
            if model_name in ready_apis:
                return True
        else:
            # Maybe the api_key was wrong.
            return False

    def is_available(model_name: str):
        # NOTE: Use KeyPathIterable
        return True if model_name in Model.AVAILABLE_MODELS else False

    def __str__(self):
        return f'Available models: {Model.AVAILABLE_MODELS}'