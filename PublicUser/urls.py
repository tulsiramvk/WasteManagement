from django.urls import path

from . import views
app_name='PublicUser'

urlpatterns = [
	path('home/', views.home),
	path('complain/',views.complaint),
	path('about/',views.about),
	path('wastepickup/',views.wastepickup),
	path('bulkpickup/',views.bulkpickup),
	path('getdumpster/',views.getdumpster),
	path('solution/',views.solution),
	path('solidwaste/',views.solidwaste),
	path('cmphistory/<int:id>/',views.cmphistory, name="cmphistory")
]