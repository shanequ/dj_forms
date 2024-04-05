
from django import forms
from django.forms import ModelForm

from .models import Client, City, Country


class ClientForm(ModelForm):

    age = forms.IntegerField(initial=24, min_value=18, max_value=120)

    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        help_text='Select a country first.'
    )

    city = forms.ModelChoiceField(
        queryset=City.objects.none(),
        help_text='Select a city after a country is selected.'
    )

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        # print('data: ', self.data)
        # print('initial: ', self.initial)
        # print('instance: ', self.instance)

        if 'country' in self.data:
            # for default value
            self.fields['city'].queryset = City.objects.filter(
                country_id=self.data.get('country'))
        elif 'country' in self.initial:
            # for initial value
            self.fields['city'].queryset = City.objects.filter(
                country_id=self.initial.get('country'))
        elif self.instance.pk:
            # for bound form
            self.fields['city'].queryset = self.instance.country.city_set.all()
        else:
            self.fields['city'].queryset = City.objects.none()

    class Meta:
        model = Client
        fields = ['username', 'first_name', 'last_name', 'age', 'country', 'city']

