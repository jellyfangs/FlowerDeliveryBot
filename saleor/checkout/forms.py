from django import forms
from django.contrib.auth.models import AnonymousUser
from django.utils.translation import ugettext_lazy as _

from ..userprofile.forms import AddressForm


class ShippingForm(AddressForm):

    use_billing = forms.BooleanField(initial=True)


class DeliveryForm(AddressForm):

    use_billing = forms.BooleanField(initial=True)


class DeliveryForm(forms.Form):

    method = forms.ChoiceField(label=_('Delivery method'))

    def __init__(self, delivery_choices, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)
        method_field = self.fields['method']
        method_field.choices = delivery_choices


# TIMELORD STUFF
from datetime import date, datetime, timedelta
from pytz import timezone
import holidays # https://github.com/ryanss/holidays.py

# Some ground rules
delivery_start_time = '10:00 AM'
delivery_end_time = '6:00 PM' # to 7:00 PM
delivery_days_range = 3
delivery_offset = 1
delivery_limits = 3

fmt = "%a %b %d %I:%M %p"
pst = 'US/Pacific'

# Time to get ill
right_now = datetime.now(timezone(pst))  # 9/11/2011
open_time = datetime.strptime(delivery_start_time, '%I:%M %p').time()
closing_time = datetime.strptime(delivery_end_time, '%I:%M %p').time()

# Check if business day
from business_calendar import Calendar, MO, TU, WE, TH, FR, SA, SU # https://github.com/antoniobotelho/py-business-calendar/
cal = Calendar(workdays=[MO,TU,WE,TH,FR,SA], holidays=holidays.US().keys())
if cal.isbusday(date.today()): 
  bump_day = 0 # 9/11
else: 
  bump_day = 1 # 9/12

# Check if delivery time
if open_time < right_now.time() < closing_time:
  start_hour = right_now.time().replace(hour=right_now.hour+1, minute=0, second=0)
else:
  start_hour = open_time
  bump_day += 1

# Set day
start_delivery_options = cal.addbusdays(date.today(), bump_day)
end_delivery_options = cal.addbusdays(start_delivery_options, delivery_days_range)

# Set time
start_delivery_options = timezone(pst).localize(datetime.combine(start_delivery_options, start_hour))
end_delivery_options = timezone(pst).localize(datetime.combine(end_delivery_options, closing_time))

#bigups https://stackoverflow.com/questions/10688006/generate-a-list-of-datetimes-between-an-interval-in-python
def rangeRover(start, end, open, close, offset):
  curr = start
  while curr.day < end.day:
    if open.hour <= curr.hour <= close.hour:
      yield curr
      curr += offset
    else:
      curr = curr.replace(day=curr.day+1)
      curr = curr.replace(hour=open.hour)

# Give me a range rover
delivery_times = []
count = 0
for result in rangeRover(start_delivery_options, end_delivery_options, open_time, closing_time, timedelta(hours=delivery_offset)):
  delivery_times.append((count, result.strftime(fmt)))
  count+=1

# Expected
"""
2015-09-08 10:00:00
2015-09-08 11:00:00
2015-09-08 12:00:00
...
2015-09-08 19:00:00
"""

class DeliveryTimeForm(forms.Form):

    delivery_time = forms.ChoiceField(choices=delivery_times, widget=forms.RadioSelect())


class ShippingForm(forms.Form):

    method = forms.ChoiceField(label=_('Shipping method'))

    def __init__(self, shipping_choices, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        method_field = self.fields['method']
        method_field.choices = shipping_choices
        if len(shipping_choices) == 1:
            method_field.initial = shipping_choices[0][1]
            method_field.widget = forms.HiddenInput()


class AnonymousEmailForm(forms.Form):

    email = forms.EmailField()
