from django.db import models


# Create your models here.

class IGL_account(models.Model):
    user_id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mobile_number = models.IntegerField(unique=True)
    IGL_username = models.CharField(max_length=30, unique=True)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    confirm_password = models.CharField(max_length=40)

    def __repr__(self):
        return self.IGL_username
