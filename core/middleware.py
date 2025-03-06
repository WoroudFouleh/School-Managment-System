from urllib import request, response

from django.utils.deprecation import MiddlewareMixin


class CustomHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['X - H'] = "Woroud"
        return response

