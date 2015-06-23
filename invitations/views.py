from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

from extra_views import UpdateWithInlinesView

from .forms import SearchForm, GuestInline
from .models import Guest, Invitation


class LookupInvitation(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def form_valid(self, form, *args, **kwargs):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        try:
            guest = Guest.objects.get(first_name_normalized=first_name,
                                      last_name_normalized=last_name)
            return redirect(guest.invitation)
        except Guest.DoesNotExist:
            form.add_error(None, 'This guest could not be found. Please try '
                           'again.')
            return self.form_invalid(form, *args, **kwargs)


class RsvpView(UpdateWithInlinesView):
    model = Invitation
    success_url = reverse_lazy('thank-you')
    template_name = 'invitation_form.html'
    slug_field = 'key'
    slug_url_kwarg = 'key'
    fields = ['hashtag_suggestion', 'song_suggestions']
    inlines = [GuestInline]
