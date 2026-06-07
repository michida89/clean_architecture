from dataclasses import dataclass, field

from domain.shared.env import get_bool_value, get_int_value, get_str_value


@dataclass(frozen=True, kw_only=True, slots=True)
class MinioConfig:
    MINIO_HOST: str = field(default_factory=lambda: get_str_value("MINIO_HOST", "localhost"))
    MINIO_PORT: int = field(default_factory=lambda: get_int_value("MINIO_PORT", 9000))
    MINIO_USER: str = field(default_factory=lambda: get_str_value("MINIO_USER", "minio"))
    MINIO_PASSWORD: str = field(default_factory=lambda: get_str_value("MINIO_PASSWORD", "minio"))
    MINIO_SECURE: bool = field(default_factory=lambda: get_bool_value("MINIO_SECURE", False))
