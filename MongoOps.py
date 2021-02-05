from pymongo import MongoClient
  
        
client = MongoClient("localhost", 27017)
db_names = client.database_names()
db = client.get_database("db_name")
col_names = db.list_collection_names
col = db.get_collection("col_name")
col.find()
col.count()
col.insert()
col.update()
col.remove()

