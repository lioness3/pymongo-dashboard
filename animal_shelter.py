from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps


class AnimalShelter():
        """ CRUD operations for Animal collection in MongoDB """
        def __init__(self, user, password):
            #Initializing the MongoClient to help access the MongoDB databases and collection
            self.user = user
            self.password = password
            #self.client = MongoClient('mongodb://127.0.0.1:45234')
            self.client = MongoClient('mongodb://%s:%s@127.0.0.1:45234/?authMechanism=DEFAULT&authSource=AAC'%(self.user , self.password))
            self.database = self.client['AAC']
           
            
  # create method that inserts a document into a specified Mongo DB and collection     
        def create(self, data):
            if data is not None:
                self.database.animals.insert(data)  # data should be dictionary
                return True;                # return true if data was created
            else:
                raise Exception("Nothing to save, because data parameter is empty")
    
  # read method queries for documents from specified Mongo DB and collection
        def read(self, data):
            if data is not None:
                cursor = self.database.animals.find(data, {'_id':False})  # return a pointer to list of results
                return cursor
            else:
                raise Exception("Nothing to read, because data was not found")
                return False
                
  # update method that queries for and updates document(s) by replacing oldInfo with newInfo
        def update(self, oldInfo, newInfo):
            if newInfo is not None:    # find and update info only if new info is given
                animal_cursor = self.read(oldInfo) # find animal object with read method
                for item in animal_cursor: # iterate through the animal object and find the animal id associated
                    animal_id = item['animal_id']
                # update the animal object based on the animal id 
                updatedInfo = self.database.animals.find_one_and_update({'animal_id':animal_id}, {'$set':newInfo})        
                return dumps(updatedInfo) #return json format of dictionary
               
            else:
                raise Exception("Nothing updated")

  # delete method that queries for and removes document(s)
        def delete(self, animal_id):
            if list(self.read({'animal_id':animal_id})) != 0:   # if the animal exists delete it
                to_be_deleted = self.database.animals.delete_one({'animal_id':animal_id})
                return to_be_deleted
            else:
                raise Exception("Nothing found to delete")
            
            

   

