from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()


@register.filter(name="author_details")
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
        return ""

    if author == current_user:
        return format_html('<strong>me</strong>')

    has_first_and_last_name = author.first_name and author.last_name
    name = f"{author.first_name} {author.last_name}" if has_first_and_last_name else f"{author.username}"

    return format_html('<a href="mailto:{}">{}</a>', author.email, name) if author.email else name