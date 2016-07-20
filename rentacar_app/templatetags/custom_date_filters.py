from django import template
import datetime

register = template.Library()

@register.filter(name='datetime_increment_days')
def datetime_increment_days(value, days_to_increment):
    end_date = value + datetime.timedelta(days=days_to_increment)
    return end_date.strftime('%d/%m/%Y')

