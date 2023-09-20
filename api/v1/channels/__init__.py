from fastapi import APIRouter

from .channels import router

channels_router = APIRouter()
channels_router.include_router(router, tags=["Channels"])

__all__ = ["channels_router"]
