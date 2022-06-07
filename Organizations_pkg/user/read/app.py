import bson
import ujson
from bson import ObjectId

from .utils import db


def retrieve_info(object_id):
    # Retrieve info from DB
    mongo = db.MongoDBConnection()
    result = list()

    with mongo:
        database = mongo.connection['mydb']
        collection = database['registrations']

        if object_id is not None:
            # Retrieve particular object
            try:
                single_object = collection.find_one({"_id": ObjectId(object_id)})
                if single_object is None:
                    return {"error": "Object id does not exist!"}
            except bson.errors.InvalidId:
                # catch the exception calling ObjectId
                return {"err": "Invalid object_id"}

            return {
                'id': object_id,
                'first_name': single_object['first_name'],
                'last_name': single_object['last_name'],
                'email': single_object['email']
            }

        else:
            # Retrieve all info
            for user in collection.find():
                result.append({
                    'id': str(user["_id"]),
                    'first_name': user['first_name'],
                    'last_name': user['last_name'],
                    'email': user['email']
                })
        return result




def lambda_handler(event, context):
    try:
        print(event)
        object_id = event['pathParameters']['id']
        # print("#######OBJECT_ID#########\n" + object_id)
    except TypeError:
        object_id = None
    except KeyError:
        object_id = None

    try:
        return {
            "statusCode": 200,
            "body": ujson.dumps({
                "message": "Success",
                "data": retrieve_info(object_id)
            })
        }
    except Exception as err:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "message": "Something went wrong. Unable to parse data !",
                "error": str(err)
            })

        }
