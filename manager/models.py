from django.db import models
from django.core.validators import RegexValidator


class UserReservation(models.Model):
    mobile_phone_re = RegexValidator(regex=r'(^\+38)?(-|\s)?(\d{3})(-|\s)?(\d{3})(-|\s)?(\d{2})(-|\s)?(\d{2})',
                                     message='Некоректно введено номер телефону.')
    name = models.CharField(max_length=50)
    num_people = models.SmallIntegerField()
    phone = models.CharField(max_length=20, validators=[mobile_phone_re])
    message = models.TextField(max_length=500, blank=True)

    is_processed = models.BooleanField(default=False)
    data_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ('-data_in', )

    def __str__(self):
        return f'{self.name}: {self.phone}: {self.message}'
