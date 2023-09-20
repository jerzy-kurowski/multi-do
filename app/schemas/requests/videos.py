from typing import Optional

from pydantic import BaseModel, constr


class VideoCreate(BaseModel):
    title: constr(min_length=1, max_length=64)
    views: int
    channel_id: int


class VideoUpdate(VideoCreate):
    title: Optional[constr(min_length=1, max_length=64)]
    views: Optional[int]
    channel_id: Optional[int]
