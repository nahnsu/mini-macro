import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class LogConfig(BaseModel):
    level: str = os.getenv("LOG_LEVEL", "INFO")
    format: str = "{time} | {level} | {message}"
    sink: str = os.getenv("LOG_SINK", "logs/mini-macro.log")
    rotation: str = "20 MB"
    retention: str = "1 month"


class APIConfig(BaseModel):
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "")
    groq_api_key: str = os.getenv("GROk_API_KEY", "")
    groq_model: str = os.getenv("GROk_MODEL", "")


class AppConfig(BaseModel):
    title: str = "Mini-Macro"
    description: str = "A FastAPI application for analyzing macronutrients"
    version: str = "0.1.0"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    api: APIConfig = APIConfig()
    log: LogConfig = LogConfig()


config = AppConfig()
