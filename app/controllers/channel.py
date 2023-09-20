from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError

from app.models import Channel
from app.repositories import ChannelRepository
from core.controller import BaseController
from core.exceptions import DuplicateValueException


class ChannelController(BaseController[Channel]):

    def __init__(self, channel_repository: ChannelRepository):
        super().__init__(model=Channel, repository=channel_repository)
        self.channel_repository = channel_repository

    async def add(self, name: str, author: str, address: str) -> Channel:
        """
        Adds a channel.

        :param name: The channel name.
        :param author: The channel author.
        :param address: The channel address.
        :return: The channel.
        """

        try:
            return await self.channel_repository.create(
                {
                    "name": name,
                    "author": author,
                    "address": address,
                }
            )
        except (IntegrityError, UniqueViolationError) as exc:
            raise DuplicateValueException(str(exc))
