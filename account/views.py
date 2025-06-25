from rest_framework.views import APIView
from .models import UserAccount
from .serializers import RegisterSerializers, DepositSerializer, WithdrawSerializer,TransferSerializer
from rest_framework.permissions import  AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            account = UserAccount.objects.create(user=user)
            token, created= Token.objects.get_or_create(user=user)
            print(token.key)
            return Response({
                "message" : "Account Created Sucessfully" ,
                "Your Account No. :" : account.id ,
                "token": token.key,
                             
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        account = UserAccount.objects.get(user=user)
        if account is None:
            return Response({"error": "Account not found."}, status=404)
        return Response({
            "account_id": account.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "current_balance": account.balance
        })

class DepositAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DepositSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            amount = serializer.validated_data.get('amount')
            user = request.user
            account = UserAccount.objects.get(user=user)
            if amount <=0 :
                return Response({"error": "Invalid amount . Please enter the valid amount"}, status=400)

            account.balance += amount
            account.save()
            return Response({
                "message": "Successfully Credited",
                "deposited_amount": amount,
                "current_balance": account.balance
            })
        return Response(serializer.errors, status=400)

class WithdrawlAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WithdrawSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            amount = serializer.validated_data.get('amount')
            user = request.user
            account = UserAccount.objects.get(user=user)
            if amount <=0 :
                return Response({"error": "Invalid amount . Please enter the valid amount"}, status=400)
            if amount >= account.balance :
                return Response({"error": "Insufficient balance"}, status=400)
            account.balance -= amount
            account.save()
            return Response({
                "message": "Successfully Debited",
                "withdrawl_amount": amount,
                "current_balance": account.balance
            })
        return Response(serializer.errors, status=400)

class DeleteAccountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        account_id = request.data.get('account_id')
        password = request.data.get('password')
        if not account_id or not password:
            return Response({"error": "Account ID and password are required."}, status=400)
        
        try:
            account = UserAccount.objects.get(id=account_id, user=user)
        except UserAccount.DoesNotExist:
            return Response({"error": "Account not found or It's not your account."}, status=400)
        
        if not user.check_password(password):
            return Response({"error": "Incorrect password."})
        user.delete()
        return Response ({"message" : "Your account is successfully deleted"})

class TransferAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer  = TransferSerializer(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            account = UserAccount.objects.get(user = user)