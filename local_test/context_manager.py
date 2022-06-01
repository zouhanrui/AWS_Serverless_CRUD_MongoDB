import bson
from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            'mongodb+srv://hanruizou:Zhr140425@cluster0.x9hei.mongodb.net/?retryWrites=true&w=majority'
        )

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def main():
    mongo = MongoDBConnection()
    with mongo:
        mydb = mongo.connection.mydb
        mycollection = mydb['mycollection']
        # print(mycollection.find())
        """
        mylist = [
            {"name": "Amy", "address": "Apple st 652"},
            {"name": "Hannah", "address": "Mountain 21"},
            {"name": "Michael", "address": "Valley 345"},
            {"name": "Sandy", "address": "Ocean blvd 2"},
            {"name": "Betty", "address": "Green Grass 1"},
            {"name": "Richard", "address": "Sky st 331"},
            {"name": "Susan", "address": "One way 98"},
            {"name": "Vicky", "address": "Yellow Garden 2"},
            {"name": "Ben", "address": "Park Lane 38"},
            {"name": "William", "address": "Central st 954"},
            {"name": "Chuck", "address": "Main Road 989"},
            {"name": "Viola", "address": "Sideway 1633"}
        ]
        mycollection.insert_many(mylist)
       
        
        
        for item in mycollection.find():
            print(item)
            
        """

        # print(mycollection.find_one({'name':'hanrui'}))

        # for user in mycollection.find():
            # print(user['name'])
        try:
            obj = mycollection.find_one({'name':'hanrui'})
            print(obj) # None
        except bson.errors.InvalidId:
            return {'err': 'Invalid input'}






if __name__ == '__main__':
    main()
