from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends

from app.controllers import VideoController
from app.filters import VideoFilter
from app.schemas.requests.videos import VideoCreate, VideoUpdate
from app.schemas.responses.videos import VideoResponse
from core.factory import Factory

router = APIRouter()


@router.post("/")
async def add_video(
        data: VideoCreate,
        controller: VideoController = Depends(Factory().get_video_controller),
) -> VideoResponse:
    return await controller.add(**data.dict())


@router.get("/")
async def list_videos(
        filters: VideoFilter = FilterDepends(VideoFilter),
        controller: VideoController = Depends(Factory().get_video_controller),
) -> list[VideoResponse]:
    return await controller.filter_and_search(filters=filters)


@router.get("/{id_}")
async def read_video(
        id_: int,
        controller: VideoController = Depends(Factory().get_video_controller),
) -> VideoResponse:
    return await controller.get_by_id(id_)


@router.patch("/{id_}")
async def patch_video(
        id_: int,
        data: VideoUpdate,
        controller: VideoController = Depends(Factory().get_video_controller),
) -> VideoResponse:
    return await controller.update_by_id(id_, data)


@router.delete("/{id_}")
async def delete_video(
        id_: int,
        controller: VideoController = Depends(Factory().get_video_controller),
):
    return await controller.delete_by_id(id_)
