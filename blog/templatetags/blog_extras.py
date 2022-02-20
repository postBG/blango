from django import template
from django.contrib.auth import get_user_model
user_model = get_user_model()


register = template.Library()

@register.filter(name="author_details")
def author_details(author):
    if not isinstance(author, user_model):
        return ""

    name = f"{author.first_name} {author.last_name}" if author.first_name and author.last_name else f"{author.username}"

    return f'<a href="mailto:{author.email}">{name}</a>' if author.email else name
