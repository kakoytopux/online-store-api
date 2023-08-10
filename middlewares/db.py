from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists

class Db:
  def __init__(self, db):
    self.__db = db
  def get_conn(self):
    engine = create_engine(self.__db)

    if not database_exists(engine.url):
      create_database(engine.url)

    return engine
  def get_session(self):
    return Session(bind=self.get_conn())
  
db = Db('mysql+pymysql://root:root123@localhost/online_store')
