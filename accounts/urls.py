from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.ClientView.as_view(),
         {'client_id': 0}, name='blank_client_form'),
    path('<int:client_id>/', views.ClientView.as_view(), name='client_form'),
    path('ajax/cities_of_country/', views.CityListOfCountry.as_view(),
         name='ajax_cities_of_country'),
]