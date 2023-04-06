"""Error handlers for the api"""

from fastapi import Request, status

from fromzero2ai.api_engine.errors.base import (
    ErrorResponseCode,
    ErrorResponseContent,
    ErrorResponse,
)


async def exception_handler(request: Request, exc: Exception) -> ErrorResponse:
    """Handle internal server errors.

    :param request: _description_
    :param exc: _description_
    :return: _description_
    """
    error_content = ErrorResponseContent(
        ErrorResponseCode.INTERNAL_SERVER_ERROR,
        message="Oops! something wrong happened.",
    )
    error_response = ErrorResponse(error_content=error_content, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return error_response
