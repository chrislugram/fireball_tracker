from django.db import models


class FireballEvent(models.Model):
    """
    This class represents a fireball event
    """

    date = models.DateTimeField()
    energy = models.FloatField(null=True, blank=True)
    impact_e = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    alt = models.FloatField(null=True, blank=True)
    vel = models.FloatField(null=True, blank=True)

    class Meta:
        """
        Meta class for FireballEvent
        """

        unique_together = ("date", "lat", "lon")
        ordering = ["-date"]

    def __str__(self):
        return f"Fireball {self.date} at ({self.lat}, {self.lon})"
