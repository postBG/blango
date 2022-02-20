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


@register.simple_tag(name="row")
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag(name="endrow")
def endrow():
    return format_html("</div>")


@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)


@register.simple_tag
def endcol():
    return format_html("</div>")


@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request = context["request"]
    current_user = request.user
    post = context["post"]
    author = post.author

    if author == current_user:
        return format_html("<strong>me</strong>")

    has_first_and_last_name = author.first_name and author.last_name
    
    name = f"{author.first_name} {author.last_name}" if has_first_and_last_name else f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)
