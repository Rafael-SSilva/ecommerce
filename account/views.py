from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.

def sign_in(request):
    if request.POST:
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('index')

    return render(request, template_name='login.html', context={})
