from pydantic import BaseModel, Field


class VideoResponse(BaseModel):
    id: int = Field(...)
    views: int = Field(...)
    title: str = Field(...)
    channel_id: int = Field(...)

    class Config:
        orm_mode = True
