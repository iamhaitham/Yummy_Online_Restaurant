import bcrypt
from django.contrib import messages
from django.shortcuts import render, redirect

import yummy_app
from . import models
from .models import User


# Create your views here.

def root(request):
    if 'loggedin' in request.session:
        return redirect('/yummy')
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        phoneno = request.POST['phone']
        user = models.usercheckexist(phoneno)
        errors = {}
        if user is None:
            errors['login'] = "User with similar account does not exist!"
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            password = request.POST['loginpwd']
        if user is not None and bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['id'] = user.id
            request.session['username'] = user.username
            request.session['loggedin'] = True
            return redirect('/welcome')
        else:
            messages.error(request, "Invalid password or email!")
    return redirect('/')


def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            username = request.POST['username']
            phone = request.POST['phone']
            password = request.POST['pwd']
            passwordc = request.POST['conf_pwd']
            if password == passwordc:
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user = models.create_user(username, phone_number=phone, city="berzeit", password=hashed_password)
                request.session['id'] = user.id
                request.session['username'] = user.username
                request.session['loggedin'] = True
                return redirect('/welcome')
    return redirect('/')


def welcome(request):
    if 'id' not in request.session:
        return redirect('/')
    return redirect("/yummy")


def logout(request):
    yummy_app.models.deleteguestcart()
    request.session.clear()
    return redirect('/yummy')
