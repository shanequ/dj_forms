
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View

from .forms import ClientForm
from .models import City, Client

from django.contrib.auth.decorators import login_required


@method_decorator(csrf_exempt, name='dispatch')
class ClientView(TemplateView):
    template_name = 'client.html'
    client_model = Client
    client_form = ClientForm

    def get_context_data(self, client_id):
        if client_id == 0:
            form = self.client_form()
        else:
            form = self.client_form(
                instance=self.client_model.objects.get(pk=client_id))

        return {'form': form, 'client_id': client_id}

    def post(selfrequest, *args, **kwargs):
        return HttpResponse('Hello!')


class CityListOfCountry(View):

    def get(self, request):
        country_id = request.GET.get('country_id')
        if country_id:
            cities = City.objects.filter(
                country_id=country_id).values_list('id', 'name')
        else:
            cities = []
        return JsonResponse(list(cities), safe=False)
