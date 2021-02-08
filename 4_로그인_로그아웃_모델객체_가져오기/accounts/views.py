from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    # GET 요청이 들어오면 login form 을 담고있는 login.html을 띄워주는 역할을 함
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')