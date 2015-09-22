from __future__ import unicode_literals

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from prices import Price
from satchless.item import ItemSet
from datetime import timedelta

class BaseDelivery(ItemSet):
    group = None
    name = ''

    def __iter__(self):
        return iter(self.group)

    def get_delivery_total(self, **kwargs):
        return Price(0, currency=settings.DEFAULT_CURRENCY)

    def get_total_with_delivery(self):
        return self.group.get_total() + self.get_delivery_total()


@python_2_unicode_compatible
class DummyShipping(BaseDelivery):
    name = 'dummy_shipping'

    def __str__(self):
        return 'Dummy shipping'

    def get_delivery_total(self, items, **kwargs):
        weight = sum(
            line.product.get_weight() * line.quantity for line in items)
        return Price(weight, currency=settings.DEFAULT_CURRENCY)


def get_delivery_options_for_items(items, **kwargs):
    if 'address' in kwargs:
        yield DummyShipping()
    else:
        raise ValueError('Unknown delivery type')


def get_delivery(name):
    return DummyShipping()


def get_delivery_times(now):
    # open today?
    import holidays
    from business_calendar import Calendar, MO, TU, WE, TH, FR, SA, SU
    cal = Calendar(workdays=[MO,TU,WE,TH,FR], holidays=holidays.US().keys())
    while not cal.isbusday(now):
        now += timedelta(days=1)
    # open now?
    start = now.replace(hour=11, minute=0, second=0, microsecond=0)
    stop = now.replace(hour=18, minute=0, second=0, microsecond=0)
    if start <= now <= stop:
        if now.minute >= 30:
            start = now + timedelta(hours=2)
            start = start.replace(minute=0, second=0, microsecond=0)
        else:
            start = now + timedelta(hours=1)
            start = start.replace(minute=0, second=0, microsecond=0)
    else:
        start = start + timedelta(days=1)
    # build today's list
    window = timedelta(hours=1)
    timeslots = []
    while start <= stop:
        timeslots.append(("{:%b %d %Y %I:%M %p}".format(start), "{:%A %I:%M %p} - {:%I:%M %p}".format(start - window, start)))
        start += window
    # build next x days' list
    next_x_days = 1
    while next_x_days <= 3:
        now += timedelta(days=1)
        start = now.replace(hour=11, minute=0, second=0, microsecond=0)
        stop = now.replace(hour=18, minute=0, second=0, microsecond=0)
        while not cal.isbusday(now):
            now += timedelta(days=1)
        while start <= stop:
            timeslots.append(("{:%b %d %Y %I:%M %p}".format(start), "{:%A %I:%M %p} - {:%I:%M %p}".format(start - window, start)))
            start += window
        next_x_days += 1
    return timeslots