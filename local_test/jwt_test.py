import jwt


def main():
    jwt_info = jwt.encode({
        "data": "payload"
    },
        "secret",
        algorithm="HS256")
    print(jwt_info)
    # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoicGF5bG9hZCJ9.JohPEXWSW0ziCf666VociqX4X76J6Pp1S8eFYRzUX8Y
    jwt_decoded = jwt.decode(jwt_info,
                             "secret",
                             algorithms="HS256")
    print(jwt_decoded)
    # "data": "payload"

if __name__ == '__main__':
    main()
