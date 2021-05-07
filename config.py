import os


class Config():
    SQLACHEMY_DATABASE_URI = os.environ['DATABASE_URL']
