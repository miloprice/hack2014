from django.conf.urls import patterns, url
from tasks import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
    url(r'^login', views.user_login, name = 'login'),
    url(r'^tasktest', views.task, name = 'tasktest'),
)
