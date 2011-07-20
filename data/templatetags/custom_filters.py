from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

def percentage(decimal):
    try:        
        return str(float(decimal))+('%')
    except ValueError:
        return 'XX'
register.filter('percentage', percentage)


def make_human_readable(value):
    return str(value.replace('_', ' ')).title()
register.filter('make_human_readable', make_human_readable)
