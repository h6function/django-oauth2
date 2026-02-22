import time

from django.contrib.auth.models import User
from django.db.models import (
    BooleanField,
    CASCADE,
    CharField,
    ForeignKey,
    IntegerField,
    Model,
    TextField,
)
from authlib.oauth2.rfc6749 import (
    AuthorizationCodeMixin,
    ClientMixin,
    TokenMixin,
    list_to_scope,
    scope_to_list,
)


def now_timestamp():
    return int(time.time())

# Create your models here.

class OAuth2Client(Model, ClientMixin):
    client_id = CharField(max_length=48, unique=True, db_index=True)
    client_secret = CharField(max_length=48, blank=True)
    client_name = CharField(max_length=120)
    redirect_uris = TextField(default='')
    default_redirect_uri = TextField(blank=False, default='')
    scope = TextField(default='')
    response_type = TextField(default='')
    grant_type = TextField(default='')
    token_endpoint_auth_method = CharField(max_length=120, default='')

    def get_client_id(self):
        return self.client_id

    def get_default_redirect_uri(self):
        return self.default_redirect_uri

    def get_allowed_scope(self, scope):
        if not scope:
            return ''
        allowed = set(scope_to_list(self.scope))
        return list_to_scope([s for s in scope.split() if s in allowed])

    def check_redirect_uri(self, redirect_uri):
        if not redirect_uri:
            return False

        if redirect_uri == self.default_redirect_uri:
            return True

        allowed = set(scope_to_list(self.redirect_uris))
        return redirect_uri in allowed

    def check_client_secret(self, client_secret):
        return self.client_secret == client_secret

    def check_endpoint_auth_method(self, method, endpoint):
        if endpoint == 'token':
            return self.token_endpoint_auth_method == method
        # TODO: developers can update this check method
        return True

    def check_response_type(self, response_type):
        allowed = self.response_type.split()
        return response_type in allowed

    def check_grant_type(self, grant_type):
        allowed = self.grant_type.split()
        return grant_type in allowed


class OAuth2AuthorizationCode(Model, AuthorizationCodeMixin):
    user = ForeignKey(User, on_delete=CASCADE)
    client_id = CharField(max_length=48, db_index=True)
    code = CharField(max_length=120, unique=True, null=False)
    redirect_uri = TextField(default='', null=True)
    response_type = TextField(default='')
    scope = TextField(default='', null=True)
    auth_time = IntegerField(null=False, default=now_timestamp)

    def is_expired(self):
        return self.auth_time + 300 < time.time()

    def get_redirect_uri(self):
        return self.redirect_uri

    def get_scope(self):
        return self.scope or ''

    def get_auth_time(self):
        return self.auth_time


class OAuth2Token(Model, TokenMixin):
    user = ForeignKey(User, on_delete=CASCADE)
    client_id = CharField(max_length=48, db_index=True)
    token_type = CharField(max_length=40)
    access_token = CharField(max_length=255, unique=True, null=False)
    refresh_token = CharField(max_length=255, db_index=True)
    scope = TextField(default='')
    revoked = BooleanField(default=False)
    issued_at = IntegerField(null=False, default=now_timestamp)
    expires_in = IntegerField(null=False, default=0)

    def get_client_id(self):
        return self.client_id

    def get_scope(self):
        return self.scope

    def get_expires_in(self):
        return self.expires_in

    def get_expires_at(self):
        return self.issued_at + self.expires_in
