from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Public, Office
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def signup(request):

	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		mob=request.POST['number']
		email=request.POST['email']
		uname=request.POST['username']
		passwd=request.POST['password']
		pic=request.FILES['pic']
		u=User(first_name=fname,last_name=lname,email=email,username=uname,password=make_password(passwd))
		u.save()
		p=Public(user=u,mobile=mob,pic=pic)
		p.save()
		return redirect('/login1/')

	return render(request,'signup.html')

def signup2(request):
	if request.method=='POST':
		email=request.POST['email']
		empID=request.POST['empID']
		contact=request.POST['contact']
		passwd=request.POST['password']
		u = User(username=empID,password=make_password(passwd))
		u.save()
		o=Office(user=u,email=email,contact=contact,)
		o.save()
		return redirect('/login2/')
	return render(request,'signup2.html')

def login1(request):
	url = '/login1/'
	if request.method=='POST':
		#print("hxbskhgshy")
		uname=request.POST['username']
		passwd=request.POST['password']
		currentUser=authenticate(username=uname,password=passwd)
		if currentUser:
			login(request,currentUser)
			u=Public.objects.get(user__username=request.user)
			return redirect('/PublicUser/home/')
		else:
			return HttpResponse('<script> alert("Invalid Username and Password");\
		window.location="%s"</script>'%url)

	return render(request, 'login1.html')
def login2(request):
	url = '/login2/'
	if request.method=='POST':
		#print("hxbskhgshy")
		empID=request.POST['empID']
		passwd=request.POST['password']
		currentUser=authenticate(username=empID,password=passwd)
		if currentUser:
			login(request,currentUser)
			o=Office.objects.get(user__username=request.user)
			return redirect('/office/home/')

		else:
			return HttpResponse('<script> alert("Invalid Employee Id and Password");\
		window.location="%s"</script>'%url)
			

	return render(request, 'login2.html')



def logout_call(request):
	logout(request)
	return redirect('/PublicUser/home/')