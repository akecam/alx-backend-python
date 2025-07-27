import os
from typing import Any
from datetime import datetime, time
from django.conf import settings
import logging

from django.core.exceptions import PermissionDenied

logger = logging.getLogger("request_logger")


class RequestLoggingMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:

        logger.info(f"{datetime.now()}-User:{request.user}-Path:{request.path}")

        response = self.get_response(request)

        return response


class RestrictAccessByTimeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request) -> Any:

        now = datetime.now().time()
        start = time(18, 0)
        end = time(21, 0)

        if start <= now <= end:
            raise PermissionDenied()
        else:
            response = self.get_response(request)
            return response
