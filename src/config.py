from dataclasses import dataclass, field
from typing import Final

from application.config import ApplicationConfig
from infrastructure.auth.config import AuthConfig
from infrastructure.database.config import DatabaseConfig
from infrastructure.minio.config import MinioConfig


@dataclass(frozen=True, kw_only=True, slots=True)
class Config:
    application: ApplicationConfig = field(default_factory=ApplicationConfig)
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    auth: AuthConfig = field(default_factory=AuthConfig)
    minio: MinioConfig = field(default_factory=MinioConfig)


config: Final[Config] = Config()
