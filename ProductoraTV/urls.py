from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	url(r'^$', views.home),
   # url(r'^login/$', views.mostrar_login),#
   
   
    

]