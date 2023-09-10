from django import template


register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def header(context):
    user  = context['request'].user
    return {
        'user': user,
    }
