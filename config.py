import os
class Config:
    """
    General configuration parent class
    """
    NEWS_API_BASE_URL=''
    NEWS_API_KEY = os.environ.get(NEWS_API_KEY)
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    """
    Production configuration child class
        Args:
            config parent class with the general app configurations
    """
    pass

class DevConfig(config):
    """
    Development configuration child class
        Args:
            config parent class with general app configurations
    """
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
