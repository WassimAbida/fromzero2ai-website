"""Health status route definition"""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from fromzero2ai.api_engine.settings import settings


router = APIRouter(prefix=settings.API_ROOT_URL)  # type: ignore


@router.get("/info")
async def info() -> JSONResponse:
    """Return the service status"""

    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
