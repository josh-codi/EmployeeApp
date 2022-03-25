from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_user
from django.contrib import messages
from django.contrib.auth.models import User

from EmployeeApp.forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
            if user is not None:
                login_user(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials provided. Please not that both fields may be case-sensitive')
               
    context={
        "form":form
    }
    return render(request, 'login.html', context)