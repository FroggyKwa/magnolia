from django.contrib import admin

from emails.models import OneTimePassword


@admin.register(OneTimePassword)
class OneTimePasswordAdmin(admin.ModelAdmin):
    pass
