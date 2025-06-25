from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserAccount,Deposit, Transfer, Withdraw

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
   
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ['account']

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['account'] = UserAccount.objects.get(user=request.user)
        return super().create(validated_data)

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'
        read_only_fields = ['account']

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['account'] = UserAccount.objects.get(user=request.user)
        return super().create(validated_data)

class TransferSerializer(serializers.ModelSerializer):

    class Meta :
        model = Transfer
        fields = '__all__'