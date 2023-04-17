"""Main application module"""

import os
import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from typing import Dict, List, Any

from fromzero2ai.api_engine import __version__
from fromzero2ai.api_engine.settings import settings
from fromzero2ai.api_engine.routes import example_route, health_status
from fromzero2ai.api_engine.errors import handlers


tags_metadata: List[Dict[str, Any]] = [
    {
        "name": "Demo API",
        "description": "Execute mathematical process using API requests",
        "externalDocs": {
            "description": "How to use the Demo API?",
            "url": "",
        },
    },
]


def create_app() -> FastAPI:
    """FASTAPI Appliction factory"""
    current_app = FastAPI(
        title=settings.API_SWAGGER_TITLE,  # type: ignore
        version=__version__,
        openapi_tags=tags_metadata,
        docs_url=os.path.join(settings.API_ROOT_URL, "documentation"),  # type: ignore
        redoc_url=os.path.join(settings.API_ROOT_URL, "redocs"),  # type: ignore
        contact={
            "name": "fromzero2ai",
            "email": "",
        },
        openapi_url=f"{settings.API_ROOT_URL}/openapi.json",
    )
    current_app.include_router(example_route.router)
    current_app.include_router(health_status.router)
    return current_app


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Demo API",
        version="0.1.0",
        description="Launch Mathematical computations.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = create_app()
app.add_exception_handler(Exception, handlers.exception_handler)
app.openapi = custom_openapi


if __name__ == "__main__":
    uvicorn.run("fromzero2ai.api_engine.main:app")
