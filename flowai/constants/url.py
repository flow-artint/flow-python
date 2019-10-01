# -*- coding: utf-8 -*-

import validators

class URL(object):

    BASE_URL        = "https://api.theflowai.com/package/"
    DASHBOARD       = "dashboard/"
    CHECK_API_KEY   = "check/api-key/"
    GET_MODEL_NAMES = "get/models/"
    INFER           = "call/ready/"

    def is_valid(url: str):
        return True if validators.url(url) else False