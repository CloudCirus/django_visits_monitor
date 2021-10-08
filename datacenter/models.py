from django.db import models
from django.utils.timezone import localtime, timedelta


def get_duration(visit):
    if visit.leaved_at:
        delta = visit.leaved_at - visit.entered_at
    else:
        delta = localtime() - visit.entered_at
    return delta


def format_duration(duration: timedelta):
    time = str(duration).split(':')
    hours = time[-3]
    minutes = time[-2]
    if duration.days:
        return f'{duration.days}д {hours}ч {minutes}мин'
    return f'{hours}ч {minutes}мин'


def is_visit_long(duration, minutes=60):
    tdelta = timedelta(minutes=minutes)
    if duration > tdelta:
        return True
    return False


class Passcard(models.Model):

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' +
            str(self.leaved_at) if self.leaved_at else 'not leaved'
        )
