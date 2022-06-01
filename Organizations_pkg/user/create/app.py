import ujson
from marshmallow import ValidationError
from .utils import db, validator

def lambda_handler(event, context):
    try:
        body = ujson.loads(event['body'])
        # ujson.loads() -> convert json to python dictionary
        # print(body['password'])
        result = validator.UserRegistrationSchema()

        # check if dictionary is empty
        res = not bool(result.validate(body))

        if res:
            # store information in DB
            mongo = db.MongoDBConnection()
            with mongo:
                database = mongo.connection['mydb']
                collection = database['registrations']
                x = result.load(body)
                print(x)
                collection.insert_one(x)

            return {
                "statusCode": 201,
                "body": ujson.dumps({
                    "message": "Registered Successfully !",
                    "data": result.validate(body)
                })
            }

        else:
            return {
                "statusCode": 400,
                "body": ujson.dumps({
                    "message": "Error!",
                    "data": result.validate(body)
                })
            }

    except ValidationError as err:
        return {
            "statusCode": 400,
            "body": ujson.dumps(({
                "message": err.messages
            }))
        }

    except KeyError:
        return {
            "statusCode": 400,
            "body": ujson.dumps(({
                "message": "Something went wrong. Unable to parse data !"
            }))
        }