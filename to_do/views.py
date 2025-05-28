from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        email = request.POST['email']

        my_user = User.objects.create_user(username, email, password)
        my_user.save()

        return redirect('/login')
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')