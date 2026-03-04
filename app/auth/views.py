from authlib.oauth2.rfc6749 import OAuth2Error
from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .auth import server
from logging import getLogger

logger = getLogger(__name__)


@require_http_methods(['GET', 'POST'])
def authorize(request: HttpRequest) -> HttpResponse:
    try:
        grant = server.get_consent_grant(request, end_user=request.user)
    except OAuth2Error as error:
        return server.handle_error_response(request, error)

    if request.method == 'GET':
        scopes = grant.client.get_allowed_scope(grant.request.payload.scope).split()
        return render(
            request,
            'auth/authorize.html',
            {'grant': grant, 'scopes': scopes},
        )

    user = authenticate(
        request,
        username=request.POST.get('username'),
        password=request.POST.get('password'),
    )

    if user:
        return server.create_authorization_response(
            request,
            grant=grant,
            grant_user=user,
        )

    return server.create_authorization_response(
        request,
        grant=grant,
        grant_user=None,
    )


@require_http_methods(['POST'])
@csrf_exempt
def issue_token(request: HttpRequest) -> HttpResponse:
    return server.create_token_response(request)
