from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends

from app.controllers import ChannelController
from app.filters import ChannelFilter
from app.schemas.requests.channels import ChannelCreate, ChannelUpdate
from app.schemas.responses.channels import ChannelResponse
from core.factory import Factory

router = APIRouter()


@router.post("/")
async def add_channel(
        data: ChannelCreate,
        controller: ChannelController = Depends(Factory().get_channel_controller),
) -> ChannelResponse:
    return await controller.add(**data.dict())


@router.get("/")
async def list_channels(
        filters: ChannelFilter = FilterDepends(ChannelFilter),
        controller: ChannelController = Depends(Factory().get_channel_controller),
) -> list[ChannelResponse]:
    return await controller.filter_and_search(filters=filters)


@router.get("/{id_}")
async def read_channel(
        id_: int,
        controller: ChannelController = Depends(Factory().get_channel_controller),
) -> ChannelResponse:
    return await controller.get_by_id(id_)


@router.patch("/{id_}")
async def patch_channel(
        id_: int,
        data: ChannelUpdate,
        controller: ChannelController = Depends(Factory().get_channel_controller),
) -> ChannelResponse:
    return await controller.update_by_id(id_, data)


@router.delete("/{id_}")
async def delete_channel(
        id_: int,
        controller: ChannelController = Depends(Factory().get_channel_controller),
):
    return await controller.delete_by_id(id_)
