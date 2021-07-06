import os
from datetime import timedelta


class Config:
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "TheUltimateSecret"
    JWT_TOKEN_LOCATION = os.environ.get("JWT_TOKEN_LOCATION") or ["headers"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
