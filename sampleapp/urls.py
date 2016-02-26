from django.conf.urls import include, url
from django.contrib import admin
from allauth import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
