from django.views.generic import TemplateView

class ClusterGraphView(TemplateView):
    template_name = 'graph.html'

    def get_context_data(self, **kwargs):
        context = super(ClusterGraphView, self).get_context_data(**kwargs)
        context['cluster_slug'] = 'ganeti'
        return context

class ClusterJsonView(TemplateView):
    template_name = 'example-graph.json'

class InstanceExtraDataView(TemplateView):
    template_name = 'instance-info.json'

