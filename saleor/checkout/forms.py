from django import forms
from django.contrib.auth.models import AnonymousUser
from django.utils.translation import ugettext_lazy as _

from ..userprofile.forms import AddressForm


class ShippingForm(AddressForm):

    use_billing = forms.BooleanField(initial=True)


class DeliveryTimeForm(forms.Form):

    time = forms.ChoiceField(label=_('Delivery time'))

    def __init__(self, available_times, *args, **kwargs):
        super(DeliveryTimeForm, self).__init__(*args, **kwargs)
        time_field = self.fields['time']
        time_field.choices = available_times
        # time_field.widget = forms.RadioSelect()


class DeliveryForm(forms.Form):

    method = forms.ChoiceField(label=_('Shipping method'))

    def __init__(self, delivery_choices, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)
        method_field = self.fields['method']
        method_field.choices = delivery_choices
        if len(delivery_choices) == 1:
            method_field.initial = delivery_choices[0][1]
            method_field.widget = forms.HiddenInput()


class AnonymousEmailForm(forms.Form):

    email = forms.EmailField()
