# Create your views here.
from django.shortcuts import render, redirect
from form_app.forms import *


def register_view(request):
    form_data = RegisterForm()
    if request.method == "POST":
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')
    return render(request, 'register.html', {'form_data': form_data})

def login_view(request):


    return render(request, 'login.html')