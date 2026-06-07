from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from infrastructure.database.config import DatabaseConfig


def build_database_url(config: DatabaseConfig) -> URL:
    return URL.create(
        drivername=config.POSTGRES_DRIVER,
        username=config.POSTGRES_USER,
        password=config.POSTGRES_PASSWORD,
        host=config.POSTGRES_HOST,
        port=config.POSTGRES_PORT,
        database=config.POSTGRES_DATABASE,
    )


class DatabaseFactory:
    def __init__(self, config: DatabaseConfig) -> None:
        self._config = config
        self._engine: AsyncEngine | None = None
        self._session_factory: async_sessionmaker[AsyncSession] | None = None

    def create_engine(self) -> AsyncEngine:
        if self._engine is None:
            self._engine = create_async_engine(
                url=build_database_url(self._config),
                echo=False,
                echo_pool=False,
                pool_size=10,
                max_overflow=20,
                pool_timeout=30,
                pool_recycle=1800,
                pool_pre_ping=True,
                connect_args={
                    "timeout": 10,
                    "command_timeout": 60,
                    "server_settings": {
                        "application_name": "project",
                        "jit": "off",
                    },
                },
            )
        return self._engine

    def create_session_factory(self) -> async_sessionmaker[AsyncSession]:
        if self._session_factory is None:
            self._session_factory = async_sessionmaker(
                bind=self.create_engine(),
                expire_on_commit=False,
            )
        return self._session_factory

    async def dispose(self) -> None:
        if self._engine is not None:
            await self._engine.dispose()
            self._engine = None
