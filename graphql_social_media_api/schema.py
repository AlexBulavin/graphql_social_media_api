import graphene
from graphene_django import DjangoObjectType
from graphql_api import models


class User(DjangoObjectType):
    class Meta:
        model = models.User

class Post(DjangoObjectType):
    class Meta:
        model = models.Post

class UserInput(graphene.InputObjectType):
    name = graphene.String()

class CreateUser(graphene.Mutation): #Создали мутатора mutator
    class Arguments:
        input = UserInput(required=True)

    ok = graphene.Boolean()
    user = graphene.Field(User)

    @staticmethod
    def mutate(root, info, input):
        isinstance = models.User(name=input.name)
        try:
            isinstance.save()
        except Exception:
            return CreateUser(ok=False, user=None)

        #Добавляем пустых followers
#        isinstance.followers.set([])
        return CreateUser(ok=True, user=isinstance)

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())
    users = graphene.List(User)

    # Необходимо определить резолвера для одного пользователя
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.User.objects.get(pk=id)
        return None

    # Необходимо определить резолвера для пользователей
    def resolve_users(self, info, **kwargs):
        #Извлекаем всех пользователей
        return models.User.objects.all()

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
