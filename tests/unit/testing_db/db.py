"""
# Python program shows the
# connection management
# for MongoDB

from pymongo import MongoClient

class MongoDBConnectionManager():
	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port
		self.connection = None

	def __enter__(self):
		self.connection = MongoClient(self.hostname, self.port)
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.connection.close()

# connecting with a localhost
with MongoDBConnectionManager('localhost', '27017') as mongo:
	collection = mongo.connection.SampleDb.test
	data = collection.find({'_id': 1})
	print(data.get('name'))


Database connection management using context manager and with statement: On executing the with block, the following operations happen in sequence:

A MongoDBConnectionManager object is created with localhost as the hostname name and 27017 as the port when the __init__ method is executed.
The __enter__ method opens the MongoDB connection and returns the MongoDBConnectionManager object to variable mongo.
The test collection in the SampleDb database is accessed and the document with _id=1 is retrieved. The name field of the document is printed.
The __exit__ method takes care of closing the connection on exiting the with block(teardown operation).

"""


from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            "mongodb+srv://hanruizou:Zhr140425@cluster0.x9hei.mongodb.net/mydb?retryWrites=true&w=majority"
        )
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
