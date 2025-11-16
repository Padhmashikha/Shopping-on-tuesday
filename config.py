import os

basedir = os.path.abspath(__file__)

class Config:

        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-in-production'

        SQLACHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance' , 'arson.db')

        SQLACHEMY_TRACK_MODIFICATION = False

        UPLOAD_FOLDER = os.path.join(basedir,'app','static','uploads')

        MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5mb

        ALLOWED_EXTENSION = {
        'png','jpg','jpeg','gif', 'webp'
        }

class DevelopmentConfig(Config):
            DEBUG = True

class ProductionConfig(Config):
            DEBUG = False


config ={
    'development': DevelopmentConfig,
    'production' : ProductionConfig,
    'default': DevelopmentConfig
}