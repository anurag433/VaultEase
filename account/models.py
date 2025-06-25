from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

class Deposit(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Withdraw(models.Model):
    account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Transfer(models.Model):
    from_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="sender")
    to_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="receiver")
    amount = models.IntegerField()
    