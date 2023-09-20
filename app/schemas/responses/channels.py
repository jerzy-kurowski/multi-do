from pydantic import BaseModel, Field


class ChannelResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    author: str = Field(
        default=None
    )
    address: str = Field(...)

    class Config:
        orm_mode = True
