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

