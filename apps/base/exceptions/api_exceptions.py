from rest_framework.exceptions import APIException


class APIError(APIException):
    def __init__(self, message=None, status=None, errors=None):
        super().__init__(detail=message, code=status)
        self.errors = errors
        self.status_code = status
