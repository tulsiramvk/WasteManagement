from django.shortcuts import render,redirect
from django.http import HttpResponse
from PublicUser.models import Complaint
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
# Create your views here.

def cmpview(request):
	cmp_data = Complaint.objects.all()
	if request.method == 'POST':
		current_status = request.POST.getlist('current_status')
		id_ = request.POST.getlist('id')
		print(id_)
		print(current_status)
		for i in range(len(id_)):
			comp = Complaint.objects.filter(id=id_[i])
			comp.update(current_status=current_status[i])
		return redirect('/office/home/')
	return render(request,'cmphistory.html', {'data':cmp_data})
	