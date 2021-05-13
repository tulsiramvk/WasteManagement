from django.db import models
from WasteManagement.models import Public



# Create your models here.
class Complaint(models.Model):
	user=models.ForeignKey (Public,on_delete=models.CASCADE)
	compType=models.CharField(max_length=20)
	location = models.CharField(max_length=20, blank=True)
	desc=models.CharField(max_length=200)
	pic=models.ImageField(upload_to='complainimage',blank=False)
	dated = models.DateTimeField(auto_now_add = True)
	current_status = models.CharField(max_length=40, blank=True)
