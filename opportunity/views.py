
from django.views.generic import DetailView, ListView

from .models import Client, Opportunity, Resource


# Create your views here.
class ClientList(ListView):
    model = Client
    template_name = 'opportunity/list.html'


class ClientDetail(DetailView):
    model = Client
    template_name = 'opportunity/detail.html'


class OpportunityList(ListView):
    model = Opportunity
    template_name = 'opportunity/list.html'


class OpportunityDetail(DetailView):
    model = Opportunity
    template_name = 'opportunity/detail.html'


class ResourceList(ListView):
    model = Resource
    template_name = 'opportunity/list.html'


class ResourceDetail(DetailView):
    model = Resource
    template_name = 'opportunity/detail.html'


# CBV Wrappers
client_list = ClientList.as_view()
client_detail = ClientDetail.as_view()

opportunity_list = OpportunityList.as_view()
opportunity_detail = OpportunityDetail.as_view()

resource_list = ResourceList.as_view()
resource_detail = ResourceDetail.as_view()
