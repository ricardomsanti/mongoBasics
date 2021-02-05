from pymongo import MongoClient


          
            
    
        
"""mo = MongoOps(client=MongoClient("localhost", 27017))
db_name = mo.new_newdb()
field_dict = mo.db_newfields()
doc_list = mo.db_newcol(field_dict)
createcol = mo.db_createcol(doc_list=doc_list, db_name=db_name)
"""
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
col.
