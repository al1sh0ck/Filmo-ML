from operator import index

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Films
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from .models import Users  # Импортируем модель пользователей
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate


def indexview(request):
    user_id = request.session.get("user_id")
    user_email = request.session.get("user_email")  # или username, если есть
    user_name = request.session.get("user_name")

    if not user_id:
        return redirect("signin")

    return render(request, "index.html", {
        "user_id": user_id,
        "user_email": user_email,
        "user_name": user_name

    })

def signin_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                request.session["user_id"] = user.id
                request.session["user_email"] = user.email
                request.session["user_name"] = user.name
                return redirect("index")
            else:
                return render(request, "signin.html", {"error": "Invalid credentials"})
        except Users.DoesNotExist:
            return render(request, "signin.html", {"error": "User not found"})

    return render(request, "signin.html")

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "create_account.html", {"error": "Passwords do not match!"})

        if Users.objects.filter(email=email).exists():
            return render(request, "create_account.html", {"error": "Email already registered!"})

        hashed_password = make_password(password)  # Хешируем пароль
        Users.objects.create(name=username, email=email, password=hashed_password)

        return redirect("signin")  # Перенаправляем на страницу входа

    return render(request, "create_account.html")
def logout_view(request):
    logout(request)
    return redirect('signin')