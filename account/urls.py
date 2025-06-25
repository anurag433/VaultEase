from django.urls import path
from .views import RegisterAPIView, DashboardAPIView, DepositAPIView, WithdrawlAPIView ,DeleteAccountAPIView, TransferAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('dashboard/', DashboardAPIView.as_view(), name='dashboard'),
    path('deposit/', DepositAPIView.as_view(), name='deposit'),
    path('withdrawl/', WithdrawlAPIView.as_view(), name='withdrawl'),  
    path('delete/', DeleteAccountAPIView.as_view(), name='delete'),
    path('transfer/',TransferAPIView.as_view(), name='transfer')

]


