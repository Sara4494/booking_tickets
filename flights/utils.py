from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data = {
            'status': 'error',
            'message': 'An error occurred.',
            'data': None,
            'errors': response.data   
        }

        response.data = custom_response_data

    return response