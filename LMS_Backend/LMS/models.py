from turtle import undo
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=150, unique=True)
    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=10, null=True, blank=True, default='none')
    user_role = models.CharField(max_length=10,default='user')
    password = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','username','password']

    def __str__(self):
        return "{}".format(self.email)


class Books(models.Model):
    book_name = models.CharField(max_length=150)
    book_author = models.CharField(max_length=150)
    book_quantity = models.IntegerField()
    book_description = models.TextField()
    borrowed_user = models.CharField(max_length=20, null=True, blank=True)
    borrowed_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
