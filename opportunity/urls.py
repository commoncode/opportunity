from django.conf.urls import patterns, url


urlpatterns = patterns(
    'opportunity.views',
    url(r'^clients/$', 'client_list', name='client_list'),
    url(r'^client/(?P<pk>\d+)$', 'client_detail', name='client_detail'),

    url(r'^opportunities/$', 'opportunity_list', name='opportunity_list'),
    url(r'^opportunity/(?P<pk>\d+)$', 'opportunity_detail', name='opportunity_detail'),

    url(r'^resources/$', 'resource_list', name='resource_list'),
    url(r'^resource/(?P<pk>\d+)$', 'resource_detail', name='resource_detail'),
)
