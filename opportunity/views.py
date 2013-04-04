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
def client_list(request):
    return ClientList.as_view()(request)


def client_detail(request, pk):
    return ClientDetail.as_view()(request, pk=pk)


def opportunity_list(request):
    return OpportunityList.as_view()(request)


def opportunity_detail(request, pk):
    return OpportunityDetail.as_view()(request, pk=pk)


def resource_list(request):
    return ResourceList.as_view()(request)


def resource_detail(request, pk):
    return ResourceDetail.as_view()(request, pk=pk)
