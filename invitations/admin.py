from django.contrib import admin
from .models import Invitation, Guest


class GuestInline(admin.TabularInline):
    model = Guest
    extra = 2


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    inlines = (GuestInline,)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'rsvp')
