from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()

@register.filter
def bootstrap(element):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("bootstrapform/field.html")
        context = Context({'field': element})
    else:
        template = get_template("bootstrapform/form.html")
        context = Context({'form': element})
        
    return template.render(context)

@register.filter
def bootstrap2(element):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("bootstrapform/field2.html")
        context = Context({'field': element})
    else:
        template = get_template("bootstrapform/form2.html")
        context = Context({'form': element})
        
    return template.render(context)

@register.filter
def bstable(element):
    element_type = element.__class__.__name__.lower()
    if element_type == 'boundfield':
        template = get_template("bootstrapform/tablefield.html")
        context = Context({'field': element})
    else:
        template = get_template("bootstrapform/tableform.html")
        context = Context({'form': element})
        
    return template.render(context)


@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"

