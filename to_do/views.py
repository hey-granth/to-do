from sqlite3 import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        email = request.POST['email']

        try:
            my_user = User.objects.create_user(username, email, password)
            messages.success(request, 'Account created successfully')
            my_user.save()
            return redirect('/login')
        except IntegrityError:
            messages.error(request, 'Username already taken')
            return render(request, 'signup.html')

    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Account logged in')
            login(request, user)
            return redirect('/todo')
        else:
            messages.error(request, 'Invalid username or password. Try Again!')
            return render(request, 'login.html')

    return render(request, 'login.html')