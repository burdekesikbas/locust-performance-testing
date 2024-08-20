class Data:

    @classmethod
    def user_create_payload(cls):
        payload = {
            "id": 5555624421,
            "username": "burdepost",
            "firstName": "burde",
            "lastName": "kesikbas",
            "email": "burde@hotmail.com",
            "password": "231312",
            "phone": "565465",
            "userStatus": 0
        }
        return payload

    @classmethod
    def headers_payload(cls):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        return headers

    @classmethod
    def params_payload(cls):
        params = {
            "username": "burde",
            "password": "123456"
        }
        return params

    @classmethod
    def create_user_with_list(cls):
        payload = [
            {
                "id": 1,
                "username": "testburde1",
                "firstName": "testburde1",
                "lastName": "testburde1",
                "email": "testburde1",
                "password": "testburde1",
                "phone": "111111",
                "userStatus": 0
            },
            {
                "id": 2,
                "username": "testburde2",
                "firstName": "testburde2",
                "lastName": "testburde2",
                "email": "testburde2",
                "password": "testburde2",
                "phone": "222222",
                "userStatus": 0
            }, {
                "id": 3,
                "username": "testburde3",
                "firstName": "testburde3",
                "lastName": "testburde3",
                "email": "testburde3",
                "password": "testburde3",
                "phone": "33333",
                "userStatus": 0
            },
            {
                "id": 4,
                "username": "testburde4",
                "firstName": "testburde4",
                "lastName": "testburde4",
                "email": "testburde4",
                "password": "testburde4",
                "phone": "444444",
                "userStatus": 0
            },
            {
                "id": 5,
                "username": "testburde5",
                "firstName": "testburde5",
                "lastName": "testburde5",
                "email": "testburde5",
                "password": "testburde5",
                "phone": "555555",
                "userStatus": 0
            }
        ]
        return payload

    @classmethod
    def create_user_with_array(cls):
        payload = [
            {
                "id": 111111111,
                "username": "testburde1",
                "firstName": "testburde1",
                "lastName": "testburde1",
                "email": "testburde1",
                "password": "testburde1",
                "phone": "111111",
                "userStatus": 0
            },
            {
                "id": 111111112,
                "username": "testburde2",
                "firstName": "testburde2",
                "lastName": "testburde2",
                "email": "testburde2",
                "password": "testburde2",
                "phone": "222222",
                "userStatus": 0
            }, {
                "id": 111111113,
                "username": "testburde3",
                "firstName": "testburde3",
                "lastName": "testburde3",
                "email": "testburde3",
                "password": "testburde3",
                "phone": "33333",
                "userStatus": 0
            },
            {
                "id": 111111114,
                "username": "testburde4",
                "firstName": "testburde4",
                "lastName": "testburde4",
                "email": "testburde4",
                "password": "testburde4",
                "phone": "444444",
                "userStatus": 0
            },
            {
                "id": 111111115,
                "username": "testburde5",
                "firstName": "testburde5",
                "lastName": "testburde5",
                "email": "testburde5",
                "password": "testburde5",
                "phone": "555555",
                "userStatus": 0
            },
            {
                "id": 111111116,
                "username": "testburde6",
                "firstName": "testburde6",
                "lastName": "testburde6",
                "email": "testburde6",
                "password": "testburde6",
                "phone": "666666",
                "userStatus": 0
            },
            {
                "id": 111111117,
                "username": "testburde7",
                "firstName": "testburde7",
                "lastName": "testburde7",
                "email": "testburde7",
                "password": "testburde7",
                "phone": "777777777",
                "userStatus": 0
            }, {
                "id": 3,
                "username": "testburde8",
                "firstName": "testburde8",
                "lastName": "testburde8",
                "email": "testburde8",
                "password": "testburde8",
                "phone": "888888",
                "userStatus": 0
            },
            {
                "id": 111111118,
                "username": "testburde8",
                "firstName": "testburde8",
                "lastName": "testburde8",
                "email": "testburde8",
                "password": "testburde8",
                "phone": "88888888",
                "userStatus": 0
            },
            {
                "id": 111111119,
                "username": "testburde9",
                "firstName": "testburde9",
                "lastName": "testburde9",
                "email": "testburde9",
                "password": "testburde9",
                "phone": "99999999",
                "userStatus": 0
            }
        ]
        return payload




