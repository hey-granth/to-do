from sqlite3 import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from to_do.models import Tasks
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        obj = Tasks(title=title, user=request.user)
        obj.save()

        result = Tasks.objects.filter(user=request.user).order_by('-date')
        return redirect('/todo', {'result': result})
    result = Tasks.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'result': result})

@login_required(login_url='/login')
def todo_edit(request, srno):
    obj = Tasks.objects.get(srno=srno)

    if request.method == 'POST':
        title = request.POST['title']
        obj.title = title
        obj.save()
        return redirect('/todo')

    return render(request, 'todo_edit.html', {'obj': obj})

@login_required(login_url='/login')
def todo_delete(request, srno):
    obj = Tasks.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo')

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('/login')