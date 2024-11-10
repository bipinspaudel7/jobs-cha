REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_RATES": {},
    "DEFAULT_RENDERER_CLASSES": [
        "base.renderers.EnhancedJSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S",
    "DATE_FORMAT": "%Y-%m-%d",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 22220,
    "EXCEPTION_HANDLER": "base.handlers.exception_handlers.exception_handler",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Rest Auth


SPECTACULAR_SETTINGS = {
    "TITLE": "Ecommerce API",
    "DESCRIPTION": "API for Ecommerce",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
