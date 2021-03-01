from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString


register = template.Library()


@register.filter(name='str_list')
@register.filter(is_safe=True)


def str_list(str):

      
    return list(str.splitlines()) 


