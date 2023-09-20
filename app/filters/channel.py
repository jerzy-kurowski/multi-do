from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from app.models import Channel


class ChannelFilter(Filter):
    name: Optional[str]
    author: Optional[str]
    address: Optional[str]
    order_by: Optional[list[str]]

    class Constants(Filter.Constants):
        model = Channel
