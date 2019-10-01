# -*- coding: utf-8 -*-

from flowai.rest.app_base     import AppBase
from flowai.rest.predictor    import Predictor
from flowai.rest.response     import Response


class FlowApp(AppBase):

    def __init__(self, api_key: str = None):
        # assertions
        # ...
        # initializations
        self.__predictor = Predictor(api_key=api_key)
        self.api_key = api_key

    def predict_by_url(self, input_url: str, model_name: str = None):
        prediction = self.__predictor.predict(input_url, model_name)
        return prediction

    def __str__(self):
        return f"""
    Instance:
        FlowApp(api_key="{self.api_key}")
    
    Methods:
        predict_by_url(input_url: str, model_name: str)"""