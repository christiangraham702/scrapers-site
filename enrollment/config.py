import os


class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-mf'
