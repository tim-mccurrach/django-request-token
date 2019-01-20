from django import template
from django.utils.html import format_html

from ..settings import JWT_QUERYSTRING_ARG
register = template.Library()


@register.simple_tag(takes_context=True)
def request_token(context):
    """Render a hidden form field containing request token."""
    request_token = context.get('request_token')
    if request_token:
        return format_html(
            '<input type="hidden" name="{}" value="{}">',
            JWT_QUERYSTRING_ARG,
            request_token
        )
    return ""


@register.simple_tag(takes_context=True)
def request_token_querystring(context):
	"""Render a query-string with the request token if it exists."""
	request = context.get('request')
	if getattr(request, 'token', None):
		return f'?{JWT_QUERYSTRING_ARG}={request.token.jwt()}'
	return ""