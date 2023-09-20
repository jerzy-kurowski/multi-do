from sqlalchemy import Select
from sqlalchemy.orm import joinedload

from app.models import Channel
from core.repository import BaseRepository


class ChannelRepository(BaseRepository[Channel]):
    """
    Channel repository provides all the database operations for the Channel model.
    """

    async def _join_videos(self, query: Select) -> Select:
        """
        Join videos.

        :param query: Query.
        :return: Query.
        """
        return query.options(joinedload(Channel.videos)).execution_options(
            contains_joined_collection=True
        )
