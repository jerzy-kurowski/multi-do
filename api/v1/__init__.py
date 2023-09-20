from fastapi import APIRouter

from .videos import videos_router
from .channels import channels_router

v1_router = APIRouter()
v1_router.include_router(videos_router, prefix="/videos")
v1_router.include_router(channels_router, prefix="/channels")
