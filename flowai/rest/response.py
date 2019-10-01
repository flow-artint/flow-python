# -*- coding: utf-8 -*-

import requests
import json


class Response:
    """Get a response from server and
    clean it for presenting it to the client.
    """

    def clean(response: requests.Response):

        # Load into dict
        response        = json.loads(response.text)['data']['demoData'] 

        # Cleaning for client
        response_dict   = {}

        for key, value in zip(response.keys(), response.values()):
            if key == "body":
                response_dict["result"] = {}
                # int index the "result" key
                for k_result, v_result in zip(response["body"].keys(), response["body"].values()):
                    response_dict["result"][int(k_result)] = v_result
            elif key == "statusCode":
                response_dict["status_code"] = response[key]
            else:
                # Set corresponding value for key
                response_dict[key] = value            

        return response_dict