from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação.

    Para gerar token:

    import secrets

    token: str = secrets.token_urlsafe(32)
    """

    API_V1_STR: str = "/api/v1"
    DB_URL: str = (
        "postgresql+asyncpg://postgres:portela@localhost:5432/faculdade"
    )
    DBBaseModel = declarative_base()

    JWT_SECRET: str = "3bpk1jcN5C8g4pnjez82N9QYShU85uF3N8OuwMkKURc"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = (
        60 * 24 * 7
    )  # 60 minutes * 24 hours *  7 days => 1 week

    class Config:
        case_sensitive = True


settings: Settings = Settings()
