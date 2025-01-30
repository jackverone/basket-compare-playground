import os
from dotenv import load_dotenv, find_dotenv

class Config:

    load_dotenv(find_dotenv())

    def __init__(self):
        self.DEBUG = False
        self.SSL_CRT = os.environ["SSL_CRT"]
        self.SSL_KEY = os.environ["SSL_KEY"]

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
