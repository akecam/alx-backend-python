import os
from typing import Any
from datetime import datetime
from django.conf import settings
import logging

logger = logging.getLogger('request_logger')

class RequestLoggingMiddleware:
    
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request) -> Any:
        
        logger.info(f"{datetime.now()}-User:{request.user}-Path:{request.path}")
        # log_path = os.path.join(settings.BASE_DIR, 'requests.log')
        # with open(log_path, 'a') as file:
        #     log = f"{datetime.now()}-User:{request.user}-Path:{request.path}\n"
            
        #     file.write(log)
        response = self.get_response(request)
        
        
        
        return response