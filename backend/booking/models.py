from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Date:
    SATURDAY = 1
    SUNDAY = 2
    MONDAY = 3
    TUESDAY = 4
    WEDNESDAY = 5
    THURSDAY = 6
    FRIDAY = 7
    
    DATE_PICK = (
        (SATURDAY, 'SATURDAY'),
        (SUNDAY, 'SUNDAY'),
        (MONDAY, 'MONDAY'),
        (TUESDAY, 'TUESDAY'),
        (WEDNESDAY, 'WEDNESDAY'),
        (THURSDAY, 'THURSDAY'),
        (FRIDAY, 'FRIDAY'),
    )


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_pick = models.PositiveSmallIntegerField(choices=Date.DATE_PICK, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.user} {self.date_pick}"
