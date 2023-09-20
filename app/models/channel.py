from sqlalchemy import BigInteger, Column, Unicode
from sqlalchemy.orm import relationship

from core.database import Base
from core.database.mixins import TimestampMixin


class Channel(Base, TimestampMixin):
    __tablename__ = "channels"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    name = Column(
        Unicode(64),
        unique=True,
        nullable=False,
    )
    author = Column(
        Unicode(64),
        nullable=True,
    )
    address = Column(
        Unicode(128),
        unique=True,
        nullable=False,
    )

    videos = relationship(
        "Video",
        back_populates="channel",
        passive_deletes=True
    )

    __mapper_args__ = {"eager_defaults": True}
