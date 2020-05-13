from django.db import models
from django.contrib.auth.models import User
import random,string
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    amount=models.BigIntegerField(default=3000)
    accountNumber=models.CharField(max_length=10,default='0123456789')#101
    def __str__(self):
        return f'{self.user.username} customer'


class Transaction(models.Model):
    transactionID=models.CharField(max_length=15,unique=True)
    dateTime=models.DateTimeField(auto_now=True)
    transactionAmount=models.BigIntegerField()
    transactionFrom=models.ForeignKey(User,on_delete=models.CASCADE,related_name='debited')
    transactionTo=models.ForeignKey(User,on_delete=models.CASCADE,related_name='credited',default=None)
    success=models.BooleanField(default=False)

    def __str__(self):
        return f'transaction from {self.transactionFrom.username} to {self.transactionTo.username}'
    