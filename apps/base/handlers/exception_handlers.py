from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.views import set_rollback

from base.exceptions.api_exceptions import APIError
from base.response import IResponse


def exception_handler(exc, context):
    errors = None
    error_message = ""
    if isinstance(exc, APIError):
        error_message = exc.detail
        errors = exc.errors
        status_code = exc.status_code
    elif isinstance(exc, exceptions.APIException):
        error = getattr(exc, "detail", None)
        status_code = exc.status_code
        if isinstance(error, str):
            error_message = error
        elif isinstance(error, dict):
            error_message = "Invalid request"
            errors = error
    elif isinstance(exc, Http404):
        exc = exceptions.NotFound()
        status_code = exc.status_code
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
        status_code = exc.status_code
    else:
        error_message = f"{exc.__class__.__name__}: {exc}"
        status_code = 500

    headers = {}

    if getattr(exc, "auth_header", None):
        headers["WWW-Authenticate"] = exc.auth_header
    if getattr(exc, "wait", None):
        headers["Retry-After"] = "%d" % exc.wait

    set_rollback()
    return IResponse(
        status=status_code,
        success=False,
        message=error_message,
        headers=headers,
        errors=errors,
    )


__all__ = [
    "exception_handler",
]
