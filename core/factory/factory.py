from functools import partial

from fastapi import Depends

from app.controllers import VideoController, ChannelController
from app.models import Video, Channel
from app.repositories import VideoRepository, ChannelRepository
from core.database import get_session


class Factory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    # Repositories
    video_repository = partial(VideoRepository, Video)
    channel_repository = partial(ChannelRepository, Channel)

    def get_channel_controller(self, db_session=Depends(get_session)):
        return ChannelController(
            channel_repository=self.channel_repository(
                db_session=db_session
            )
        )

    def get_video_controller(self, db_session=Depends(get_session)):
        return VideoController(
            video_repository=self.video_repository(db_session=db_session)
        )


