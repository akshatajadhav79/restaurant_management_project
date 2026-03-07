from django.shortcuts import render
from utils.validation_utils import validate_email_address
from rest_framework.response import response
# Create your views here.

def resgister_user(request):
    email = request.data.get("email")

    if not validate_email_address(email):
        return response({"error":"Invalid email address"},status = 400)
