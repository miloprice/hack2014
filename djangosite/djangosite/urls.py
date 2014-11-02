from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from tasks import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^tasktest/', include('tasks.urls')),
)
