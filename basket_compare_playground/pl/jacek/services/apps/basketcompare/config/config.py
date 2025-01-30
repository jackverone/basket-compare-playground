import os
from dotenv import load_dotenv, find_dotenv

class Config:

    load_dotenv(find_dotenv())

    def __init__(self):
        self.DEBUG = False

    SSL_CRT = os.environ["SSL_CRT"]
    SSL_KEY = os.environ["SSL_KEY"]

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
