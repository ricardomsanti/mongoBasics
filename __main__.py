

  dash = "------------------------------------------------------------------------------------"
    client = MongoClient("localhost", 27017)    
           
    #intro 
    def say_hi(self):
        print("\n"
                "MongoDB Ops Started\n" +
                str(self.dash) + "\n"
                "Please choose how you want to proceeed\n"
              )
    
    
    #database
    def set_database(self, db):    
        db = client[db]sdds
    
    
    
    
m = Menu()

m.say_hi()

#--------------------------------------------------------

from pymongo import MongoClient


#document
doc = {"teste": 1}

#colletcion

collections = db.collections.insert_one(doc)   
