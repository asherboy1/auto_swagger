
from pymysql.cursors import DictCursor

from common.config_handler import config
from common.db_handler import DBHandler


class MyDBHandler(DBHandler):
    def __init__(self, **kw):

        super().__init__(
            host=config.read('db', 'host'),
            port=eval(config.read('db', 'port')),
            user=config.read('db', 'user'),
            password=config.read('db', 'password'),
            charset=config.read('db', 'charset'),
            cursorclass=DictCursor,
            **kw
        )