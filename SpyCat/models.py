from django.core.validators import MinValueValidator
from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    years_of_experience = models.PositiveIntegerField(blank=False, null=False)
    breed = models.CharField(max_length=255, blank=False, null=False)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        validators=[MinValueValidator(0)],
    )

    def __str__(self):
        return f"{self.name} - {self.breed}"

    class Meta:
        verbose_name = "Spy Cat"
        verbose_name_plural = "Spy Cats"
