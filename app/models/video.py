from sqlalchemy import BigInteger, Column, Unicode, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base
from core.database.mixins import TimestampMixin


class Video(Base, TimestampMixin):
    __tablename__ = "videos"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    views = Column(
        BigInteger,
        nullable=True
    )
    title = Column(
        Unicode(64),
        nullable=False,
        unique=True
    )
    channel_id = Column(
        BigInteger,
        ForeignKey("channels.id", ondelete="CASCADE"),
        nullable=False
    )
    channel = relationship(
        "Channel",
        uselist=False,
        back_populates="videos",
    )

    __mapper_args__ = {"eager_defaults": True}
