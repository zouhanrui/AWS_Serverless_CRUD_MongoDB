from marshmallow import Schema, fields, post_load, ValidationError
from argon2 import PasswordHasher
from . import db

def encrypt(plain_text_password):
    """ This function retuens the hash value of password """
    ph = PasswordHasher()
    hashed_password = ph.hash(plain_text_password)
    return hashed_password


class UserRegistrationSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

    def encrypt_password(self):

