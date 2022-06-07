"""
Defining two functions:
1. Create new JWT token
2. Refresh token: generate a new token based on previous token validity till it hasn't expired

"""
import datetime
import os
import jwt
# json web token: self-contained way for securely transmitting information between parties as json obj
from marshmallow import ValidationError


def create_access_token(result):
    # Returns new JWT token (encoded:xxxxx.yyyyy.zzzzz: header.payload.signature)
    jwt_info = jwt.encode({
        "id": str(result['_id']),
        "first_name": result['first_name'],
        "last_name": result['last_name'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=900)
        },
            os.environ['SECRET_KEY'],
            algorithm="HS256")

    return jwt_info


def refresh_token(token):
    # Refresh Token if it has expired
    try:
        result = jwt.decode(token, os.environ['SECRET_KEY'], algorithms="HS256")
        jwt_info = jwt.encode({
            **result,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=300)
            # extend 5 mins for current token
            },
                os.environ['SECRET_KEY'])
        print("refreshed token: " + jwt_info)
        return {
            "status": True,
            "data": jwt_info,
            "message": None
        }
    except jwt.exceptions.DecodeError:
        return {
            "status": False,
            "data": None,
            "message": "Unable to decode data"
        }
    except jwt.ExpiredSignatureError:
        return {
            "status": False,
            "data": None,
            "message": "Token expired"
        }


