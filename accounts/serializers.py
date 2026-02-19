from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CustomTokenSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token
    

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def save(self,*args, **kwargs):
        refresh_token = self.validated_data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()