from django.db import models
from django.core.validators import RegexValidator


class UserContact(models.Model):
    email_re = RegexValidator(regex=r'^[a-zA-Z0-9](-?[a-zA-Z0-9_])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$',
                              message='Некоректно введено пошту.')
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[email_re])
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    is_processed = models.BooleanField(default=False)
    data_in = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-data_in',)

    def __str__(self):
        return f'{self.name}: {self.email}: {self.message}'
