from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/metrics/', include('app_metrics.urls')),
)
