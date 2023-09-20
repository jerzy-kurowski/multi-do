from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from app.models import Video


class VideoFilter(Filter):
    title: Optional[str]
    channel_id: Optional[int]
    order_by: Optional[list[str]]

    class Constants(Filter.Constants):
        model = Video
