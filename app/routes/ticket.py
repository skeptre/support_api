from fastapi import APIRouter
from typing import Any

router = APIRouter()

@router.get("/tickets")
async def get_tickets() -> list[dict[str, Any]]:
    return []
