from django.conf.urls import patterns, include, url
from django.contrib import admin
from news import views as news

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newstest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', news.login),
    url(r'^logout/$', news.logout),
    url(r'^$', news.feed),
    url(r'^admin/', include(admin.site.urls)),
)
