from fastapi import APIRouter

from proxy.server.api import io

# main app REST API router
router = APIRouter()

router.include_router(io.router)


@router.get(
    '/',
    summary='Example base route'
)
async def get_info() -> str:
    return "Root route example"
