from django.shortcuts import render

# Create your views here.

def login_user(request):
    return render(request, template_name='login.html', context={})
