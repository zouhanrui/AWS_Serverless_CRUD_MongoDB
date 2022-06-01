import ujson
from marshmallow import ValidationError
from .utils import validator


def lambda_handler(event, context):
    try:
        body = ujson.loads(event['body'])
        login_schema = validator.UserLoginSchema()

        # check if body is empty
        error = login_schema.validate(body)
        not_error = not bool(error)

        if not_error:
            return {
                "statusCode": 200,
                "body": ujson.dumps({
                    "msg": "Welcome!",
                    "data": {
                        "token": login_schema.load(body)['token']
                    }
                })
            }
        else:
            return {
                "statusCode": 400,
                "body": ujson.dumps({
                    "msg": "Error! Invalid input, email(Email class) + password(Str) required! ",
                    "data": error
                })
            }

    except ValidationError as err:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "msg": err.messages
            })
        }
    except KeyError:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "msg": "Something went wrong. unable to parse data!"
            })
        }


def token_refresh(event, context):
    try:
        body = ujson.loads(event['body'])
        print(type(body)) # dict
        refresh_token_schema = validator.RefreshTokenSchema()
        error = refresh_token_schema.validate(body)
        is_err = bool(error)
        # print(is_err)
        # print(refresh_token_schema.load(body))

        if not is_err:
            return {
                "statusCode": 200,
                "body": ujson.dumps({
                    "msg": None,
                    "data": refresh_token_schema.load(body)
                    # Schema.load(data) > data is a dictionary
                    # Schema.loads(data) > data is a json string
                })
            }
        else:
            return {
                "statusCode": 400,
                "body": ujson.dumps({
                    "msg": "Error! Invalid Token input",
                    "data": error
                })
            }

    except ValidationError as err:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "msg": err.messages
            })
        }
    except KeyError:
        return {
            "statusCode": 400,
            "body": ujson.dumps({
                "msg": "Something went wrong. unable to parse data!"
            })
        }