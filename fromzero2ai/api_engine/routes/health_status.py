"""Health status route definition"""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from fromzero2ai.api_engine.settings import settings


router = APIRouter()


@router.get("/service-status")
async def health_check_route() -> JSONResponse:
    """Return the service status"""
    return JSONResponse(status_code=status.HTTP_200_OK, content="Service healthy.")


@router.get("/")
async def root():
    return JSONResponse(status_code=status.HTTP_200_OK, content="Welcome to the Home Page of this API.")
