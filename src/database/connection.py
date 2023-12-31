import pymongo

class Database:
  def __init__(self, conn, db_name, db_coll):
    self.connection = pymongo.MongoClient(conn)
    self.db = self.connection[db_name]
    self.coll = self.db[db_coll]

  def query_check_id(self, obj):
    return self.coll.find_one(obj)

  def query_store_films(self, obj):
    return self.coll.insert_one(obj.__dict__)
