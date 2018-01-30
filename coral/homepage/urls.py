from django.conf.urls import url
from homepage import views

urlpatterns = [

	url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()),
	url(r'^funfacts/$', views.FunFactsPageView.as_view())


]

