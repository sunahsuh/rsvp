from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from invitations.views import LookupInvitation, RsvpView

urlpatterns = [
    url(r'^$', LookupInvitation.as_view(), name='lookup'),
    url(r'^(?P<key>[[\w]{32})/$', RsvpView.as_view(), name='rsvp'),
    url(r'^thanks/$',
        TemplateView.as_view(template_name='thanks.html'),
        name='thank-you'),
    url(r'^admin/', include(admin.site.urls)),
]
