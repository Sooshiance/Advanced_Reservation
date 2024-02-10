from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Date:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    
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
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=144, unique=True, primary_key=True)
    description = models.CharField(max_length=244)

    def __str__(self) -> str:
        return f"{self.title}"


class Cart(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    item      = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_pick = models.PositiveSmallIntegerField(choices=Date.DATE_PICK, validators=[])
    peak      = models.DurationField()
    
    def __str__(self) -> str:
        return f"{self.user} {self.item} {self.peak}"
    
    class Meta:
        unique_together = ["peak", "date_pick"]


class Order(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE)
    description = models.CharField(max_length=244, null=True, blank=True)
    
    @property
    def get_user_role(self):
        return self.user.role
    
    def __str__(self) -> str:
        return f"{self.user} {self.cart}"
