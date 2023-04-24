"""Health status route definition"""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from fromzero2ai.api_engine.settings import settings
from fromzero2ai.math_engine.addition import math_addition
from fromzero2ai.math_engine.multiplication import math_multiplication

router = APIRouter(prefix=settings.API_ROOT_URL)  # type: ignore


@router.post("/addition")
async def addition(a: int, b: int) -> JSONResponse:
    """Return the math addition of two numbers."""
    return math_addition(a, b)


class Item(BaseModel):
    a: int
    b: int

@router.post("/multiplication")
async def multiplication(item:Item) -> JSONResponse:
    """Return the math multiplication of two numbers."""

    return JSONResponse(status_code=status.HTTP_200_OK,
     content={"result":math_multiplication(item.a, item.b)})
