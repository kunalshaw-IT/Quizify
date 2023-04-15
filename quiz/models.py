from django.db import models

# Create your models here.
class questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=30,null=True)
    option2 = models.CharField(max_length=30,null=True)
    option3 = models.CharField(max_length=30,null=True)
    option4 = models.CharField(max_length=30,null=True)
    answer = models.CharField(max_length=30,null=True)


class player(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    points = models.CharField(max_length=30,null=True)