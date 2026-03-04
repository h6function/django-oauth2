from django.contrib import admin
from .models import OAuth2Client, OAuth2Token, OAuth2AuthorizationCode

# Register your models here.

@admin.register(OAuth2Client)
class OAuth2ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_name', 'get_default_redirect_uri')
    search_fields = ('client_id', 'client_name')

@admin.register(OAuth2Token)
class OAuth2TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'client_id', 'token_type', 'access_token', 'scope', 'revoked')
    search_fields = ('user__username', 'client_id')
    raw_id_fields = ('user',)

@admin.register(OAuth2AuthorizationCode)
class OAuth2AuthorizationCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'client_id', 'code', 'redirect_uri', 'response_type', 'scope', 'auth_time')
    search_fields = ('user__username', 'client_id', 'code')
    raw_id_fields = ('user',)
