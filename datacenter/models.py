from django.db import models
from django.utils import timezone
from datetime import timedelta


def format_duration(duration):
    """Takes timedelta and format it to str"""

    return str(duration)


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
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def _get_duration_by_now(self):
        current_time = timezone.localtime()
        return round((current_time - self.entered_at).total_seconds())

    def get_duration(self):
        if not self.leaved_at:
            return timedelta(seconds=self._get_duration_by_now())
        else:
            return self.leaved_at - self.entered_at

    def is_long(self, minutes=60):
        delta = self.get_duration()
        return delta > timedelta(minutes=minutes)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
