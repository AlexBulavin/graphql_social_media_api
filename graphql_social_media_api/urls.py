"""graphql_social_media_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),

    #Для исключения проверки csrf
    #path("graphql", GraphQLView.as_view(graphiql=True)),

    #подробности здесь: https://docs.graphene-python.org/projects/django/en/latest/installation/
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    #Для включения и использования проверки необходимо: https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax

]

