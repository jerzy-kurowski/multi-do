from typing import Optional

from pydantic import BaseModel, constr


class ChannelCreate(BaseModel):
    name: constr(min_length=1, max_length=64)
    author: constr(min_length=1, max_length=64)
    address: constr(min_length=1, max_length=128)


class ChannelUpdate(ChannelCreate):
    name: Optional[constr(min_length=1, max_length=64)]
    author: Optional[constr(min_length=1, max_length=64)]
    address: Optional[constr(min_length=1, max_length=128)]
