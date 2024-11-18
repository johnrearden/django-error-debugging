from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    content = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}, who is {"content" if self.content else "a troublemaker"}'

    
