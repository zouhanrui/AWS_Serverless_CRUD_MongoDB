from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            'mongodb+srv://hanruizou:<password>@cluster0.x9hei.mongodb.net/?retryWrites=true&w=majority'
        )

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def main():
    mongo = MongoDBConnection()
    with mongo:
        mydb = mongo.connection.mydb
        mycollection = mydb['mycollection']
        print(mycollection.find())
        for item in mycollection.find():
            print(item)



if __name__ == '__main__':
    main()
