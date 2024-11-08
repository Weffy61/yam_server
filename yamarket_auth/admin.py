from django.contrib import admin

from yamarket_auth.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['username', 'tg_username', 'subscription']


