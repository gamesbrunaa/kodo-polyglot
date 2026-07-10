from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = "my_database"
    db_user: str = "root"
    db_password: str = ""
    app_env: str = "development"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
