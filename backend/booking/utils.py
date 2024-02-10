from django.utils.timezone import datetime
from django.core.exceptions import ValidationError


def isPassed(obj):
    if obj < datetime.now().weekday():
        raise ValidationError("")
    return obj 
