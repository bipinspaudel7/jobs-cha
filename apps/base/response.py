from rest_framework import status as http_status
from rest_framework.response import Response


class IResponse(Response):
    """
    This class is used to override the default Response class
    """

    def __init__(
        self,
        data=None,
        success=True,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        message=None,
        meta=None,
        errors=None,
    ):
        super().__init__(data, status, template_name, headers, exception, content_type)
        self.data = {
            "success": success,
            "data": data,
            "message": message,
            "errors": errors,
            "meta": meta,
        }


class SuccessResponse(IResponse):
    """
    This class is used to override the default Response class
    """

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        message=None,
        meta=None,
        errors=None,
    ):
        super().__init__(
            data,
            True,
            status=status,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
            message=message,
            meta=meta,
            errors=errors,
        )


class ForbiddenResponse(IResponse):
    """
    This class is used to override the default Response class
    """

    def __init__(
        self,
        data=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        message=None,
        meta=None,
        errors=None,
    ):
        super().__init__(
            data,
            False,
            http_status.HTTP_403_FORBIDDEN,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
            message=message,
            meta=meta,
            errors=errors,
        )


class NotFoundResponse(IResponse):
    """
    This class is used to override the default Response class
    """

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        message=None,
        meta=None,
        errors=None,
    ):
        super().__init__(
            data,
            False,
            http_status.HTTP_404_NOT_FOUND,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
            message=message,
            meta=meta,
            errors=errors,
        )


class ErrorResponse(IResponse):
    """
    This class is used to override the default Response class
    """

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        message=None,
        meta=None,
        errors=None,
    ):
        super().__init__(
            data,
            False,
            http_status.HTTP_400_BAD_REQUEST,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
            message=message,
            meta=meta,
            errors=errors,
        )


class InternalServerErrorResponse(IResponse):
    """
    This class is used to override the default Response class
    """

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
        message=None,
        meta=None,
        errors=None,
    ):
        super().__init__(
            data,
            False,
            http_status.HTTP_500_INTERNAL_SERVER_ERROR,
            template_name=template_name,
            headers=headers,
            exception=exception,
            content_type=content_type,
            message=message,
            meta=meta,
            errors=errors,
        )
