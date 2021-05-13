from django.shortcuts import render, redirect
from .models import Complaint
from WasteManagement.models import Public
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from . models import Complaint
from django.http import HttpResponse

# Create your views here.

def cmphistory(request,id):
	p = Public.objects.get(user__id=id)
	c = Complaint.objects.filter(user_id=p.id)
	url = '/PublicUser/complain'
	if len(c)>0:

		return render(request,'publiccmphistory.html',{'object_list': c})
	else:
		return HttpResponse('<script> alert("No Complaint Found!");\
		window.location="%s"</script>'%url)


def home(request):
	return render(request, 'Public.html')


@login_required(login_url = '/login1/')
def complaint(request):
	if request.method=='POST':
		complain=request.POST['complain']
		location = request.POST['location']
		desc=request.POST['desc']
		pic=request.FILES['pic']
		curr_status = request.POST['current_status']
		uObj=Public.objects.get(user__username=request.user)
		o= Complaint(user=uObj,compType=complain,desc=desc,pic=pic,location=location, current_status=curr_status)
		o.save()
		return redirect('/PublicUser/home/')
	return render(request,'complain.html')
	

def about(request):
	return render(request,'about.html')
def wastepickup(request):
	return render(request,'2nd.html')
def bulkpickup(request):
	return render(request,'3rd.html')
def getdumpster(request):
	return render(request,'1st.html')
def solution(request):
	return render(request,'4th.html')
def solidwaste(request):
	return render(request,'5th.html')
