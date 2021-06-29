from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=2500)
    followers = models.ManyToManyField('graphql_api.User')

class Post(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

