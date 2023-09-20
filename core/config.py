from enum import Enum

from pydantic import BaseSettings, PostgresDsn, RedisDsn


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    WORKERS_NUM: int = 1
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    DATABASE_URL: PostgresDsn = (
        "postgresql+asyncpg://user:password@127.0.0.1:5432/db-name"
    )
    REDIS_URL: RedisDsn = "redis://localhost:6379/7"
    RELEASE_VERSION: str = "0.1"
    SHOW_SQL_ALCHEMY_QUERIES: int = 0
    SECRET_KEY: str = "super-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24


config: Config = Config()
