from django.shortcuts import render, redirect


# Create your views here.


def sys_admin_login(request):
    return render(request, "base/admin_login.html")


def sys_admin_page(request):
    return render(request, "sys_admin/index.html")


def sys_admin_logout(request):
    return redirect("sys_admin_login")


def sys_admin_all_users(request):
    return render(request, "sys_admin/all_users.html")


def sys_admin_all_images(request):
    return render(request, "sys_admin/all_images.html")


def sys_admin_profile(request):
    return render(request, "sys_admin/sys_admin_profile.html")
