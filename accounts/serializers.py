from rest_framework import  serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ('username', 'password' , 'password2')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')

        if password1 != password2:
            raise serializers.ValidationError("Password and confirm password doesn't matched")
        return attrs


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'