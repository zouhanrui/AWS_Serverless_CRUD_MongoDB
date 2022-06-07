import json
import pytest
import time
from Organizations_pkg.user.create import app
from tests.unit.testing_db import db


@pytest.fixture()
def fixture_event():
    return {
        "body": "{\"first_name\": \"testy\", \"last_name\": \"test\", "
                "\"email\": \"testuser" + str(time.time_ns()) + "@test.cn\", \"password\": \"password\"}"
    }


class TestRegistrationAPI:
    def test_lambda_handler(self, fixture_event):
        ret = app.lambda_handler(fixture_event, "")
        data = json.loads(ret['body'])

        assert ret['statusCode'] == 201
        assert "message" in ret['body']
        assert data['message'] == "Registered Successfully !"


    def teardown(self):
        mongo = db.MongoDBConnection()
        with mongo:
            database = mongo.connection['mydb']
            collection = database['registrations']

            # Get last inserted id
            queryset = collection.find().sort([("_id", -1)]).limit(1)
            for result in queryset:
                result_id = result['_id']

            # drop last inserted id
            collection.delete_one({"_id": result_id})

