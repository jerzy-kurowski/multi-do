from sqlalchemy import Select
from sqlalchemy.orm import joinedload

from app.models import Video
from core.repository import BaseRepository


class VideoRepository(BaseRepository[Video]):
    """
    Video repository provides all the database operations for the Video model.
    """

    async def get_by_channel_id(
        self, channel_id: int, join_: set[str] | None = None
    ) -> list[Video]:
        """
        Get all videos by channel id.

        :param channel_id: The channel id to match.
        :param join_: The joins to make.
        :return: A list of videos.
        """
        query = await self._query(join_)
        query = await self._get_by(query, "video_channel_id", channel_id)

        return await self._all(query)

    async def _join_channel(self, query: Select) -> Select:
        """
        Join the channel relationship.

        :param query: The query to join.
        :return: The joined query.
        """
        return query.options(joinedload(Video.channel))
