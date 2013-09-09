from django.conf.urls import patterns, include, url
from views import ClusterGraphView, ClusterJsonView, InstanceExtraDataView


# Since this is a test Django project a fixed cluster slug is used.
cluster_slug = '(?P<cluster_slug>[-_A-Za-z0-9]+)'

validfqdnregex = "(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])"
instance_hostname = '(?P<instance_hostname>%s)'%(validfqdnregex,)

urlpatterns = patterns('',

    url(r'^$',ClusterGraphView.as_view(),name='cluster-graph'),

    url(r'^ganetiviz/cluster/%s/$' % cluster_slug, ClusterJsonView.as_view(),
        name='json-cluster'),

    url(r'^ganetiviz/%s/%s/$' % (cluster_slug,instance_hostname),
        InstanceExtraDataView.as_view(), name='instance-info'),
)
