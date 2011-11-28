from django.conf.urls.defaults import patterns, url

from app_metrics.views import *

urlpatterns = patterns('',
    url(
        regex=r'^reports/$',
        view=metric_report_view,
        name='app_metrics_reports',
        ),
)
