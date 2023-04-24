"""Health status route definition"""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from fromzero2ai.api_engine.settings import settings
from fromzero2ai.math_engine.addition import math_addition

router = APIRouter(prefix=settings.API_ROOT_URL)  # type: ignore


@router.post("/addition")
async def addition(a: int, b: int) -> JSONResponse:
    """Return the service status"""
    return math_addition(a, b)
