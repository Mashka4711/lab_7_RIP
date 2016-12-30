from django.db import models
from django.contrib.auth.models import AbstractUser


class ServiceModel (models.Model):
    id = models.AutoField(primary_key=True)
    service_price = models.CharField(max_length=20)
    service_type = models.CharField(max_length=40)
    service_class_of_price = models.CharField(max_length=20)
    ord_num = models.ManyToManyField('OrderModel')


class User(AbstractUser):
    phone = models.CharField(max_length=15, default='')
    address = models.TextField(verbose_name='Адрес', default='')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    order_num = models.IntegerField(unique=True)
    order_date = models.DateField()
    user_id = models.ForeignKey(User)

    def __str__(self):
        return str(self.order_num)