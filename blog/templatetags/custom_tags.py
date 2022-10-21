from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag(takes_context=True)
def get_categories(context):
    # return Category.objects.filter(language=context["request"].LANGUAGE_CODE)
    return Category.objects.all()
