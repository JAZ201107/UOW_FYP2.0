from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect("user_home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("user_home")
            else:
                messages.info(request, "Username Or password is not correct")
                return redirect("user_login")
        return render(request, "base/login.html")


def user_register(request):
    if request.user.is_authenticated:
        return redirect("user_home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data["username"]
                messages.success(request, "Account Created Successfully For " + user)
                return redirect('')
        context = {
            'form': form
        }
        return render(request, "user/register.html", context=context)


@login_required(login_url="user_login")
def user_home(request):
    return render(request, "user/index.html")


@login_required(login_url="user_login")
def user_logout(request):
    logout(request)
    return render(request, "base/login.html")


@login_required(login_url="user_login")
def user_history(request):
    logout(request)
    return render(request, "user/history.html")


@login_required(login_url="user_login")
def user_profile(request):
    return render(request, "user/profile.html")


@login_required(login_url="user_login")
def user_IoT(request):
    return render(request, 'user/IoT.html')


@login_required(login_url="user_login")
def user_upload(request):
    return render(request, "user/upload.html")
