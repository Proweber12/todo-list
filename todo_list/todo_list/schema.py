from graphene import ID, Field, Int, List, Mutation, ObjectType, Schema, String
from graphene_django import DjangoObjectType

from todoapp.models import Project, Todo
from usersapp.models import User


class UsersType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class TodosType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = "__all__"


class ProjectsType(DjangoObjectType):
    class Meta:
        model = Project
        fields = "__all__"


class Query(ObjectType):
    all_users = List(UsersType)
    all_todos = List(TodosType)
    all_projects = List(ProjectsType)

    user_by_username = Field(UsersType, username=String(required=True))
    todo_by_id = Field(TodosType, id=Int(required=True))
    project_by_name = Field(ProjectsType, name=String(required=True))

    todo_by_user = List(TodosType, username=String(required=True))
    todo_by_project = List(TodosType, name=String(required=True))
    project_by_user = List(ProjectsType, username=String(required=True))

    # Users
    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_username(root, info, username=None):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    # TODO`s
    def resolve_all_todos(root, info):
        return Todo.objects.all()

    def resolve_todo_by_id(root, info, id=None):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return None

    def resolve_todo_by_user(root, info, username=None):
        todos = Todo.objects.all()
        if username:
            todo = todos.filter(creator__username=username)
        return todo

    def resolve_todo_by_project(root, info, name=None):
        todos = Todo.objects.all()
        if name:
            todo = todos.filter(project__name=name)
        return todo

    # Projects
    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_project_by_name(root, info, name=None):
        try:
            return Project.objects.get(name=name)
        except Project.DoesNotExist:
            return None

    def resolve_project_by_user(root, info, username=None):
        projects = Project.objects.all()
        if username:
            project = projects.filter(users__username=username)
        return project


class UserUpdateMutation(Mutation):
    class Arguments:
        id = ID()
        username = String(required=False)
        first_name = String(required=False)
        last_name = String(required=False)
        email = String(required=False)

    user = Field(UsersType)

    @classmethod
    def mutate(cls, root, info, id, username, first_name, last_name, email):
        user = User.objects.get(id=id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return UserUpdateMutation(user=user)


class TodoUpdateMutation(Mutation):
    class Arguments:
        id = ID()
        text = String(required=False)
        creator = Int(required=False)
        project = Int(required=False)

    todo = Field(TodosType)

    @classmethod
    def mutate(cls, root, info, id, text, creator, project):
        todo = Todo.objects.get(id=id)
        todo.text = text
        todo.creator_id = creator
        todo.project_id = project
        todo.save()
        return TodoUpdateMutation(todo=todo)


class ProjectUpdateMutation(Mutation):
    class Arguments:
        id = ID()
        name = String(required=False)
        link = String(required=False)

    project = Field(ProjectsType)

    @classmethod
    def mutate(cls, root, info, id, name, link):
        project = Project.objects.get(id=id)
        project.name = name
        project.link = link
        project.save()
        return ProjectUpdateMutation(project=project)


class Mutations(ObjectType):
    update_user = UserUpdateMutation.Field()
    update_todo = TodoUpdateMutation.Field()
    update_project = ProjectUpdateMutation.Field()


schema = Schema(query=Query, mutation=Mutations)


# Готовые запросы на получение данных

# {
# allUsers{
#   id
#   username
#   firstName
#   lastName
#   isActive
#   todoSet{
#     text
#   }
# }
# userByUsername(username:"admin"){
#   username
#   lastName
# }
# allTodos{
#   id
#   text
#   create
#   update
#   creator {
#     id
#     username
#     firstName
#   }
#   project{
#     id
#     name
#     link
#   }
# }
# todoById(id:2){
#   id
#   text
#   creator{
#     username
#   }
# }
# todoByUser(username:"Max69"){
#   text
# }
# todoByProject(name:"Кирпич"){
#   text
#   isActive
# }
# allProjects{
#   id
#   name
#   link
# }
#   projectByName(name:"Кирпич"){
#   name
#   link
# }
# projectByUser(username:"Petya23"){
#   name
#   link
# }
# }

# Готовые мутации

# mutation updateUser{
#   updateUser(id:2,username:"Petya32", firstName:"Пётр",lastName:"Иванов", email:"petr12341@gmail.com"){
#     user{
#       username
#       firstName
#       lastName
#       email
#     }
#   }
# }

# mutation updateTodo {
#   updateTodo(id: 4, text: "Разложить кирпич", creator: 2, project: 2) {
#     todo {
#       id
#       text
#       creator{
#         id
#         username
#       }
#       project{
#         id
#         name
#       }
#     }
#   }
# }

# mutation updateProject {
#   updateProject(id: 2, name: "Камень", link:"https://docs.graphene-python.org/projects/django/en/latest/filtering/") {
# 		project{
#       id
#       name
#       link
#     }
#   }
# }
