from authlib.integrations.django_oauth2 import AuthorizationServer
from authlib.oauth2.rfc6749 import grants
from logging import getLogger
from .models import OAuth2AuthorizationCode, OAuth2Client, OAuth2Token

logger = getLogger(__name__)


class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    def save_authorization_code(self, code, request):
        return OAuth2AuthorizationCode.objects.create(
            code=code,
            client_id=request.client.client_id,
            redirect_uri=request.payload.redirect_uri,
            response_type=request.payload.response_type,
            scope=request.payload.scope,
            user=request.user,
        )

    def query_authorization_code(self, code, client):
        logger.debug("Querying authorization code: %s for client_id: %s", code, client.client_id)
        try:
            item = OAuth2AuthorizationCode.objects.get(code=code, client_id=client.client_id)
        except OAuth2AuthorizationCode.DoesNotExist:
            logger.warning("Authorization code not found: %s", code)
            return None

        if not item.is_expired():
            return item

    def delete_authorization_code(self, authorization_code):
        authorization_code.delete()

    def authenticate_user(self, authorization_code):
        return authorization_code.user


server = AuthorizationServer(
    client_model=OAuth2Client,
    token_model=OAuth2Token,
)

# register grants
server.register_grant(AuthorizationCodeGrant)
