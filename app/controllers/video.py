from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError

from app.models import Video
from app.repositories import VideoRepository
from core.controller import BaseController
from core.exceptions import DuplicateValueException


class VideoController(BaseController[Video]):
    """Video controller."""

    def __init__(self, video_repository: VideoRepository):
        super().__init__(model=Video, repository=video_repository)
        self.video_repository = video_repository

    async def get_by_channel_id(self, channel_id: int) -> list[Video]:
        """
        Returns a list of videos based on channel_id.

        :param channel_id: The channel id.
        :return: A list of videos.
        """

        return await self.video_repository.get_by_channel_id(channel_id)

    async def add(self, title: str, views: int, channel_id: int) -> Video:
        """
        Adds a video.

        :param title: The video title.
        :param views: The video views.
        :param channel_id: The video channel_id.
        :return: The channel.
        """

        try:
            return await self.video_repository.create(
                {
                    "title": title,
                    "views": views,
                    "channel_id": channel_id,
                }
            )
        except (IntegrityError, UniqueViolationError) as exc:
            raise DuplicateValueException(str(exc))
