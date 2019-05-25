from django.db import models


class Plate(models.Model):
    owner = models.ForeignKey('auth.User', related_name='plates', on_delete=models.CASCADE)
    plate = models.CharField(max_length=7)
    created = models.DateTimeField(auto_now_add=True)
    insurance = models.BooleanField(default=True)
    stolen = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.plate
