from django.db import models


class Invitation(models.Model):
    hashtag_suggestion = models.CharField(max_length=255, blank=True)
    song_suggestions = models.TextField(blank=True)

    def __str__(self):
        name = str(self.guest_set.first())
        count = self.guest_set.count()
        return '{} ({})'.format(name, count)


class Guest(models.Model):
    invitation = models.ForeignKey(Invitation)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rsvp = models.NullBooleanField(default=None)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
