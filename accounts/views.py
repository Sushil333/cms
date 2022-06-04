from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import RegisterUserSerializer
from rest_framework import permissions

class RegisterUserApi(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args,  **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"data": "Registration Successful"})
        return Response(serializer.errors)