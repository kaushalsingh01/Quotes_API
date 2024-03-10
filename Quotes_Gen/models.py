from django.db import models

# Create your models here.
class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    quotes = models.TextField()
    given_by = models.CharField(max_length = 100, blank=True, null=True)

    def __str__(self):
        return self.quotes

