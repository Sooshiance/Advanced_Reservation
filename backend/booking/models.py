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


class Item(models.Model):
    title = models.CharField(max_length=144, unique=True, primary_key=True)
    description = models.CharField(max_length=244)

    def __str__(self) -> str:
        return f""


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    date_pick = models.PositiveSmallIntegerField(choices=Date.DATE_PICK)
    peak = models.DurationField()
    
    class Meta:
        unique_togather = ["peak", "date_pick"]
