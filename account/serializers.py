from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAccount

class RegisterSerializers(serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = [ "username", "first_name" ,"last_name", "email", "password"]

    def create(self,validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
    
class UserAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAccount
        fields = ["id", "first_name", "last_name", "username", "email", "balance"]
    