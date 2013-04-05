
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'opportunity.views',
    url(r'^client/$', 'client_list', name='client-list'),
    url(r'^client/(?P<pk>\d+)$', 'client_detail', name='client-detail'),

    url(r'^opportunity/$', 'opportunity_list', name='opportunity-list'),
    url(r'^opportunity/(?P<pk>\d+)$', 'opportunity_detail', name='opportunity-detail'),

    url(r'^resource/$', 'resource_list', name='resource-list'),
    url(r'^resource/(?P<pk>\d+)$', 'resource_detail', name='resource-detail'),
)
