from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    #     return HttpResponse('<h4>HI</h4>')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return HttpResponse('<h4>HI</h4>')
            return redirect('pok')
            # return render(request, 'log_web/home.html')
        else:
            messages.info(request, 'Пароль или имя пользователя некоректны')

    context = {}
    return render(request, 'log_web/login.html', context)

def pok(request):
    return render(request, 'log_web/home.html')
