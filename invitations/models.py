from django.db import models


class Invitation(models.Model):
    hashtag_suggestion = models.CharField(max_length=255, blank=True)
    song_suggestions = models.TextField(blank=True)


class Guest(models.Model):
    invitation = models.ForeignKey(Invitation)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rsvp = models.NullBooleanField()
