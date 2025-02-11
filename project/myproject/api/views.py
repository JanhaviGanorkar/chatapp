from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

User = get_user_model()

@api_view(["POST"])
def register_user(request):
    """Registers a new user"""
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(email=email, password=make_password(password))
    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")  # ✅ Use email instead of username
        password = data.get("password")
        
        user = authenticate(request, email=email, password=password)  # ✅ Authenticate using email
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful", "user": {"email": user.email}})
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)
    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def logout_view(request):
    logout(request)  # Ends the session
    return JsonResponse({"message": "Logged out"}, status=200)

def csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def user_info(request):
    return JsonResponse({"username": request.user.username, "email": request.user.email})
