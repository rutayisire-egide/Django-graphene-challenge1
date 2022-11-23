import graphene
from graphene_django import DjangoObjectType
from Users.models import UserModel

class UsersType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = '__all__'


class ListUsers(graphene.ObjectType):
    users = graphene.List(UsersType)

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()

class AddUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String()
    
    user = graphene.Field(UsersType)

    @classmethod
    def mutate(cls,root,info,name,email,phone):
        user = UserModel()
        user.name = name
        user.email = email
        user.phone = phone
        user.save()
        return AddUser(user=user)

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()

schema = graphene.Schema(query=ListUsers, mutation=Mutation)

