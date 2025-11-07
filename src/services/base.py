from src.db_conf.db_context_manager import DBManager


class BaseService:
    db: DBManager

    def __init__(self, db: DBManager):
        self.db = db

