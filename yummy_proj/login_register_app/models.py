from django.db import models


# TODO Fix imports


# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['username']) < 2:
            errors["username"] = "User name should be at least 2 characters"

        if len(postData['pwd']) < 8:
            errors["passwordlen"] = "Password should be at least 8 characters"

        if postData['pwd'] != postData['conf_pwd']:
            errors["passwordmatch"] = "Password and Password confirmation don't match! "
        return errors


class User(models.Model):
    username = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    # orders=
    # cart
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()  # add this line!


def create_user(username, phone_number, city, password):
    return User.objects.create(username=username, phone_number=phone_number, city=city, password=password)


def usercheckexist(phone_number):
    users = User.objects.filter(phone_number=phone_number)
    if len(users) > 0:
        return users[0]
    else:
        return None


