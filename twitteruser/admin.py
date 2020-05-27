from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitteruser.models import TwitterUser


class AccountAdmin(UserAdmin):
    list_display = ('username')
    search_fields = ('username')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(TwitterUser, UserAdmin)
