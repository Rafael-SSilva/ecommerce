from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.

def sign_in(request):
    context = {}
    if request.POST:
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('index')
        context['errors'] = ['No account found for the e-mail provided.','please check the email.']
    return render(request, template_name='login.html', context=context)
