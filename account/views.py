from django.shortcuts import render
from utils.validation_utils import validate_email_address
from rest_framework.response import response
from .serializers import UserProfileSerializer
from rest_framework import status
from rest_framework import viewsets,permissions 
# Create your views here.

def resgister_user(request):
    email = request.data.get("email")

    if not validate_email_address(email):
        return response({"error":"Invalid email address"},status = 400)

class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticate]

    def update(self,request,pk = None):
        user = request.user
        if str(user.id) ! = pk:
            return Response(
                {
                    "error":"You can only update your own profile"
                },status = status.HTTP_403_FORBIDDEN 
            )
        serializer = UserProfileSerializer(user,data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"Profile updated successfully ","data":serializer.data},
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)