import bson
import ujson
from bson import ObjectId

from .utils import db


def lambda_handler(event, context):
    try:
        object_id = event['pathParameters']['id']
    except TypeError:
        object_id = None
    except KeyError:
        object_id = None

    mongo = db.MongoDBConnection()
    with mongo:
        database = mongo.connection['mydb']
        collection = database['registrations']
        try:
            collection.delete_one({'_id': ObjectId(object_id)})
            return {
                "statusCode": 204,
                "body": ujson.dumps({
                    "msg": "Deleted Successfully!",
                    "data": None
                })
            }

        except bson.errors.InvalidId:
            # catch the exception calling ObjectId
            return {"err": "Invalid object_id"}
