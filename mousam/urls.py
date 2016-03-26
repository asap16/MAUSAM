from django.conf.urls import url
from mousam import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^result/', views.result_page, name ='result_page'),
]