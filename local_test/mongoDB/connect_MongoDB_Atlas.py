from pymongo import MongoClient

# https://www.w3schools.com/python/python_mongodb_getstarted.asp

# Connect your application to your cluster using MongoDB's native drivers

cluster = 'mongodb+srv://hanruizou:<password>@cluster0.x9hei.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(cluster)

print(client.list_database_names())

db = client.mydb
print(db)

# create a collection
mycollection = db['mycollection']
mydict = { "name": "hanrui", "address": "Highway 99" }
x = mycollection.insert_one(mydict)
print(x)
#db.createCollection('newCollection')

print(db.list_collection_names())
