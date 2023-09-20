from fastapi import APIRouter

from .videos import router

videos_router = APIRouter()
videos_router.include_router(router, tags=["Videos"])

__all__ = ["videos_router"]
