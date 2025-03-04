from fastapi import APIRouter, Depends
from mcp_bridge.openapi_tags import Tag
from mcp_bridge.auth import get_api_key

from .tools import router as tools_router
from .prompts import router as prompts_router
from .resources import router as resources_router
from .server import router as server_router

router = APIRouter(prefix="/mcp", tags=[Tag.mcp_management], dependencies=[Depends(get_api_key)])

router.include_router(tools_router)
router.include_router(prompts_router)
router.include_router(resources_router)
router.include_router(server_router)
