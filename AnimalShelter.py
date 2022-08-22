#The import that allows for server connections to Mongo
from pymongo import MongoClient

#The import that allows for querying with an ObjectID
from bson.objectid import ObjectId

#The class that contains all the definitions needed for CRUD
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, aacuser, passwordPrompt()):
        # Initializing the MongoClient using the specified path to my port 
        self.client = MongoClient('mongodb://localhost:36452/AAC' % (aacuser, passwordPrompt()))
        #Setting the AAC database to be worked from
        self.database = self.client['AAC']

# The method to implement the C in CRUD.
    def create(self, data):
        #Checks to see if the data is null or empty and returns false in either case
        if data is not None: 
            if data:
                self.database.animals.insert_one(data)
                return True
        else:
            return False

# The method to implement the R in CRUD.
    def read(self, search):
        #Checks to see if the data is null or empty and returns exception in either case
        if search is not None: 
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            exception = "Nothing to search, because search parameter is empty"
            return exception
        
# The method to implement the U in CRUD.
    def update(self, save):
        if save is not None:
        # the save() method updates the document if this has an _id property 
        # which appears in the collection, otherwise it saves the data
        # as a new document in the collection
            if save:
                saveResult = self.database.animals.insert_one(save)
            return saveResult
        else:
            exception = "Nothing to update, because save parameter is None"
            
# The method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if remove:
                removeResult = self.database.animals.delete_one(remove)
        else:
            exception: "Nothing to delete, because remove parameter is None"
        
        
#Test data
data_1 = {"age_upon_outcome": "5 months",

            "animal_id": "A333333",

            "animal_type": "Dog",

            "breed": "English Bulldog",

            "color": "Brown and Black",

            "date_of_birth": "07/21/20",

            "datetime": "2020-07-21 10:49:00",

            "monthyear": "2020-07-21T10:49:00",

            "name": "Arenaj",

            "outcome_subtype": "Foster",

            "outcome_type": "Adoption",

            "sex_upon_outcome": "Unneutered Male",

            "location_lat": 33.60384687,

            "location_long": -97.35033333,

            "age_upon_outcome_in_weeks": 28.9642246428357}

data_2 = {"age_upon_outcome": "6 months",

            "animal_id": "A333334",

            "animal_type": "Dog",

            "breed": "Sheba",

            "color": "Black",

            "date_of_birth": "01/18/20",

            "datetime": "2020-01-18 10:49:00",

            "monthyear": "2020-01-18T10:49:00",

            "name": "Seasons",

            "outcome_subtype": "Foster",

            "outcome_type": "Adoption",

            "sex_upon_outcome": "Neutered Male",

            "location_lat": 343.60987687,

            "location_long": -97.35034533,

            "age_upon_outcome_in_weeks": 28.1234246428357}

data_3 = {"age_upon_outcome": "8 months",

            "animal_id": "A333335",

            "animal_type": "Dog",

            "breed": " Siberian Husky",

            "color": "Deep Grey",

            "date_of_birth": "01/03/20",

            "datetime": "2020-01-03 10:49:00",

            "monthyear": "2020-01-03T10:49:00",

            "name": "Bless",

            "outcome_subtype": "Foster",

            "outcome_type": "Adoption",

            "sex_upon_outcome": "Neutered Male",

            "location_lat": 33.60382947,

            "location_long": -97.35054321,

            "age_upon_outcome_in_weeks": 72.9642246428357}



search = {"animal_id" : "A333333"}
assignment = AnimalShelter
assignment.__init__(assignment,"aacuser", "passwordPrompt()")

success = assignment.create(assignment, data_1)
print(success)
results = assignment.read(assignment, search)
print(results)

save = {"animal_id" : "A333333"}
assignment = AnimalShelter
assignment.__init__(assignment,"aacuser", "passwordPrompt()")

success = assignment.update(assignment, data_2)
print(success)
results = assignment.read(assignment, save)
print(results)

remove = {"animal_id" : "A333333"}
assignment = AnimalShelter
assignment.__init__(assignment,"aacuser", "passwordPrompt()")

success = assignment.delete(assignment, data_3)
print(success)
results = assignment.read(assignment, remove)
print(results)
