from operator import index

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Films
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from .models import Users  # Импортируем модель пользователей

def get_films(request):
    films = Films.objects.all().values("name", "image", "length", "genre")
    return JsonResponse(list(films), safe=False)
def indexview(request):
    return render(request, "index.html")

def signin_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Users.objects.get(email=email)  # Проверяем, есть ли пользователь в базе
            if check_password(password, user.password):  # Проверяем хешированный пароль
                request.session["user_id"] = user.id  # Сохраняем ID пользователя в сессии
                return redirect("films")  # Перенаправляем на страницу фильмов
            else:
                error_message = "Invalid email or password."
        except Users.DoesNotExist:
            error_message = "User not found."

        return render(request, "signin.html", {"error": error_message})

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