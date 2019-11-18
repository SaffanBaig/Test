from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, CompanyRegisterForm, CompanyLoginForm
from django.contrib.auth import get_user_model, authenticate, login

def user_login_page(request):
    form = UserLoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            print("ERROR")
    print(request.user.is_authenticated)
    return render(request, 'accounts/user/login.html', context)

def company_login_page(request):
    form = CompanyLoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        else:
            print("ERROR")
    return render(request, 'accounts/company/login.html', context)

User = get_user_model()
def user_register_page(request):
    form = UserRegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(name=username,email=email,password=password)
    return render(request, 'accounts/user/register.html', context)

def company_register_page(request):
    form = CompanyRegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        compname = form.cleaned_data.get("compname")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        location = form.cleaned_data.get("location")
        new_user = User.objects.create_staffuser(name=compname,email=email,password=password,location=location)
    return render(request, 'accounts/company/register.html', context)