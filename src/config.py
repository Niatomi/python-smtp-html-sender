from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class ModifiedSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', case_sensitive=False,
    extra='ignore')

class SMTPSettings(ModifiedSettings):

    login: str = Field(alias='SMTP_LOGIN')
    password: str = Field(alias='SMTP_PASSWORD')

smtp_config = SMTPSettings()
