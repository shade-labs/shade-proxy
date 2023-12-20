from fastapi import APIRouter

from proxy .server.api import io, shade

router = APIRouter()

router.include_router(io.router, prefix='/io')
router.include_router(shade.router, prefix='/shade')


@router.get(
    '/',
    summary='Root info'
)
async def get_info() -> str:
    return "Any root information"
