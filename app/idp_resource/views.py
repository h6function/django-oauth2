from authlib.integrations.django_oauth2 import ResourceProtector, BearerTokenValidator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from logging import getLogger
from auth.models import OAuth2Token

logger = getLogger(__name__)

require_oauth = ResourceProtector()
require_oauth.register_token_validator(BearerTokenValidator(OAuth2Token))

# Create your views here.

@require_http_methods(['GET'])
@require_oauth('user.email')
def user_email(request):
    user = request.oauth_token.user
    return JsonResponse({
        'id': user.pk,
        'email': user.email,
    })


@require_http_methods(['GET'])
@require_oauth('user.name')
def user_name(request):
    user = request.oauth_token.user
    return JsonResponse({
        'id': user.pk,
        'first_name': user.first_name,
        'last_name': user.last_name,
    })
