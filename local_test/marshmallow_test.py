import datetime as dt
from marshmallow import Schema, fields, post_load
from pprint import pprint
import json


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def post_loaded(self, data, **kwargs):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def main():
    user1 = User(name='hanrui', email='hanrui@gmail.com')
    user2 = User(name='difu', email='difu@gmail.com')
    user3 = User(name='alex', email='abc')
    schema = UserSchema()
    result = schema.dump([user1, user2], many=True)
    # pprint(result)
    json_result = schema.dumps(user1)
    # pprint(json_result)
    # print(user1.__repr__())
    error = schema.validate(user3.email)
    # print(error)
    result2 = schema.dump(user2)
    error2 = schema.validate(result2)
    # print(error2)  # {}
    # print(bool(error2))  # False

    result3 = schema.dump(user3)
    error3 = schema.validate(result3)
    # print(error3)  # {'email': ['Not a valid email address.']}
    # print(bool(error3))  # True
    dic = {"name": "sadfasdfasdf",
           "email": "hanrui@lsdkajf.com"}
    json_str = json.dumps(dic)
    schema.loads(json_str)


if __name__ == '__main__':
    main()
