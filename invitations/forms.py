from django import forms

from extra_views import InlineFormSet

from .models import normalize, Guest


class SearchForm(forms.Form):
    first_name = forms.CharField(label='Your first name', max_length=50)
    last_name = forms.CharField(label='Your last name', max_length=50)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return normalize(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return normalize(last_name)


class RsvpCustomBooleanField(forms.NullBooleanField):
    widget=forms.RadioSelect(
        choices=((True, 'Attending'), (False, 'Not Attending'))
    )
    def has_changed(self, initial, data):
        if initial is not None:
            initial = self.to_python(initial)
        if data is not None:
            data = self.to_python(data)
        return initial != data


class GuestForm(forms.ModelForm):
    rsvp = RsvpCustomBooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['rsvp'].label = 'Response'

    def clean(self, *args, **kwargs):
        vals = super(GuestForm, self).clean(*args, **kwargs)
        print(vals)
        return vals

    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'rsvp')


class GuestInline(InlineFormSet):
    model = Guest
    form_class = GuestForm
    can_delete = False
    extra = 0
    fields = ('first_name', 'last_name', 'rsvp')
