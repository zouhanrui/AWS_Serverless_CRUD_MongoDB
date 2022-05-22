from pymongo import MongoClient



# Connect your application to your cluster using MongoDB's native drivers

cluster = 'mongodb+srv://hanruizou:<password>@cluster0.x9hei.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(cluster)

print(client.list_database_names())

db = client.mydb

print(db.list_collection_names())

