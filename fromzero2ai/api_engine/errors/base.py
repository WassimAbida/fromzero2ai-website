"""Custom errors for the api"""

from fastapi.responses import JSONResponse


class ErrorResponseCode:
    """Define the standard error response codes."""

    INTERNAL_SERVER_ERROR = "Internal server error"


class ErrorResponseContent:
    """Error response content class."""

    def __init__(self, code: str, message: str):
        """Define the error content"""
        self.content = {"code": code, "message": message}


class ErrorResponse(JSONResponse):
    """Error response json object."""

    def __init__(self, *args, error_content: ErrorResponseContent, **kwargs):
        """Define the json error response"""
        super().__init__(*args, content=error_content.content, **kwargs)
