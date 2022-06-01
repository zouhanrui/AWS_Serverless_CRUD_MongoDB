import bson
import ujson
from bson import ObjectId

from .utils import db, validator

def lambda_handler(event, context):
    try:
        object_id = event['pathParameters']['id']
    except TypeError:
        object_id = None
    except KeyError:
        object_id = None

    body = ujson.loads(event['body'])
    # ujson.loads() --> convert json obj to python dictionary

    result = validator.UserSchema()
    error = result.validate(body)
    is_err = bool(error)

    if not is_err:
        mongo = db.MongoDBConnection()
        with mongo:
            database = mongo.connection['mydb']
            collection = database['registrations']

            try:
                collection.update_one({'_id': ObjectId(object_id)}, {"$set": body})

                return {
                    "statusCode": 200,
                    "body": ujson.dumps({
                        "msg": "Updated Successfully!",
                        "data": result.dump(body)
                    })
                }

            except bson.errors.InvalidId:
                return {
                    "statusCode": 400,
                    "body": ujson.dumps({
                        "msg": "Error! Invalid ObjectId",
                        "data": None
                    })
                }
    else:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "msg": "Error! ",
                "data": error
            })
        }





