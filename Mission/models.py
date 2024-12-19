from django.db import models


class Mission(models.Model):
    cat = models.ForeignKey(
        "SpyCat.SpyCat", on_delete=models.CASCADE, null=True, blank=True
    )
    targets = models.ManyToManyField("Target")
    complete = models.BooleanField(default=False)


class Target(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
