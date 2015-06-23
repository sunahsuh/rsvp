from uuid import uuid4 as uuid

from django.db import models


def get_key():
    return uuid().hex


class Invitation(models.Model):
    key = models.CharField(max_length=32, default=get_key)
    hashtag_suggestion = models.CharField(
        verbose_name='Wedding Hashtag Suggestion',
        max_length=255,
        blank=True
    )
    song_suggestions = models.TextField(blank=True)

    def __str__(self):
        name = str(self.guest_set.first())
        count = self.guest_set.count()
        return '{} ({})'.format(name, count)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('rsvp',
                       args=[self.key])


def normalize(value):
    return value.replace(
        '.', ''
    ).replace(
        ' ', ''
    ).lower()


class Guest(models.Model):
    invitation = models.ForeignKey(Invitation)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name_normalized = models.CharField(max_length=255, blank=True)
    last_name_normalized = models.CharField(max_length=255, blank=True)
    rsvp = models.NullBooleanField(default=None)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def save(self):
        self.first_name_normalized = normalize(self.first_name)
        self.last_name_normalized = normalize(self.last_name)
        print(self.rsvp)
        super(Guest, self).save()
