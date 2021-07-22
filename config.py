import os
from pathlib import Path


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Random_TEXTUjhfjhj'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(Path().absolute(), 'stock.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
