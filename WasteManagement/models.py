from django.db import models
from django.contrib.auth.models import User

class Public(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	mobile=models.CharField(max_length=12)
	pic =models.ImageField(upload_to='proimage',blank=True)


class Office(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email=models.CharField(max_length=30)
	contact=models.CharField(max_length=12)