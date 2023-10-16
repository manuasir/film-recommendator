import pymongo

class Database:
  def __init__(self, conn, db_name, db_coll):
    self.connection = pymongo.MongoClient(conn)
    self.db = self.connection[db_name]
    self.coll = self.db[db_coll]