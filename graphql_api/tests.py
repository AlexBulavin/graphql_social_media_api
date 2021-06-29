from graphene_django.utils import GraphQLTestCase
# Create your tests here.

class GraphQLUserTest(GraphQLTestCase):
    fixtures = ['users.json']
    def test_retrieve_by_id(self):
        expected = {
              "data": {
                "user": {
                  "id": "2",
                  "name": "Dan Bilzerian",
                  "followers": [
                    {
                      "name": "John Doe"
                    }
                  ]
                }
              }
            }

        res = self.query("""{
            user(id: 2) {
              id
              name
              followers {
                name
              }
            }
        }""")
        #Первая проверка на статус код, который возвращает сервер
        self.assertEqual(res.status_code, 200)

        #Следующая проверка на соответствие выдаваемого результата ожидаемому
        self.assertEqual(expected, res.json())

    def test_create_user(self):
        expected = {
            "data": {
                "createUser": {
                    "ok": True,
                    "user": {
                        "id": "3",
                        "name": "Ivan Maskin",
                    }
                }
            }
        }

        res = self.query(
            """
            mutation createUser {
              createUser(input: {
                name: "Ivan Maskin"
              }) {
                 ok
                 user {
                   id
                   name
                 }
              }
            }
            """
        )

        #Первая проверка на статус код, который возвращает сервер
        self.assertEqual(res.status_code, 200)

        #Следующая проверка на соответствие выдаваемого результата ожидаемому
        self.assertEqual(expected, res.json())

    def test_retrieve_user_with_posts(self):
       expected = {
           "data": {
               "user": {
                   "id": "2",
                   "name": "Dan Bilzerian",
                   "followers": [
                       {
                           "name": "John Doe"
                       }
                   ],
                   "postSet": [
                       {
                          "content": "I love to party!!!"
                       }
                   ]
               }
           }
       }

       res = self.query(
           """
           { 
               user(id:2) {
                    id
                    name
                    followers {
                        name
                    }
                    postSet {
                        content
                    }
               }
           }    
           """
       )
       # Первая проверка на статус код, который возвращает сервер
       self.assertEqual(res.status_code, 200)

       # Следующая проверка на соответствие выдаваемого результата ожидаемому
       self.assertEqual(expected, res.json())

    def test_list_users(self):
        res = self.query(
            """
            {
                users {
                    name
                    }
            }
            """
        )
        # Первая проверка на статус код, который возвращает сервер
        self.assertEqual(res.status_code, 200)

        # Следующая проверка на количество пользователей. Их должно быть два на стабовых данных.
        self.assertEqual(len(res.json()["data"]["users"]), 2)