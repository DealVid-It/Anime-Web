from django.db import models


class Poll(models.Model):
    CHOICE_AUDIO = [
        ('SUB', 'Sub'),
        ('DUB', 'Dub'),
    ]

    name = models.CharField(max_length=50)
    anime = models.CharField(max_length=100)
    subORdub = models.CharField(
        max_length=3, choices=CHOICE_AUDIO, default='DUB')
