from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^employees/$', views.EmployeeList.as_view()),
	url(r'^employees/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view()),
]