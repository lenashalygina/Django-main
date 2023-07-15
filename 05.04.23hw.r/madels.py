from django.db import models

class Rating(models.Model):
    value = models.PositiveIntegerField(default=0, choices=[(i, i) for i in range(1, 11)])

    def __str__(self):
        return str(self.value)
