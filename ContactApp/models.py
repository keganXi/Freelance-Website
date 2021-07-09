from django.db import models

# Create your models here.


class ClientContactDatabase(models.Model):
    full_name = models.TextField(max_length=50)
    company_name = models.TextField(max_length=50)
    email = models.CharField(max_length=50)
    referrel = models.TextField()
    message = models.TextField(max_length=50)

    def __str__(self):
        return self.full_name

