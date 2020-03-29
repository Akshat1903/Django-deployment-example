from django import template

register = template.Library()

@register.filter(name='cut')
#this is python decorator method

def cut(value,arg):
    """
    This cuts out all the values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)     this is method 1
