import datetime as dt
from marshmallow import Schema, fields
from pprint import pprint


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


def main():
    user1 = User(name='hanrui', email='hanrui@gmail.com')
    user2 = User(name='difu', email='difu@gmail.com')
    schema = UserSchema()
    result = schema.dump([user1, user2], many=True)
    pprint(result)
    json_result = schema.dumps(user1)
    pprint(json_result)
    # print(user1.__repr__())


if __name__ == '__main__':
    main()
