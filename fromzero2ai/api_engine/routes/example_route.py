"""Health status route definition"""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from fromzero2ai.api_engine.settings import settings


router = APIRouter(prefix=settings.API_ROOT_URL)  # type: ignore


@router.get("/info")
async def info() -> JSONResponse:
    """Return the service status"""

    return {
        "api_name": settings.API_NAME,
    }
