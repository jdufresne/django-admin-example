from django.db import models
from django.urls import reverse


class SoftDeletedModelManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(deleted=False)


class SoftDeletedModel(models.Model):
    value = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)

    objects = SoftDeletedModelManager()
    allobjects = models.Manager()


class ManyInstancesModel(models.Model):
    value1 = models.CharField(max_length=100, blank=True)
    value2 = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse("admin:myapp_manyinstancesmodel_change", args=(self.pk))


class StackedModel(models.Model):
    parent = models.ForeignKey(ManyInstancesModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    datetime = models.DateTimeField(blank=True)


class TabularModel(models.Model):
    parent = models.ForeignKey(ManyInstancesModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, help_text="The model's text")
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    datetime = models.DateTimeField(blank=True)


class ForeignKeyModel(models.Model):
    parent = models.ForeignKey(ManyInstancesModel, on_delete=models.CASCADE)
    other = models.ForeignKey(
        ManyInstancesModel, on_delete=models.CASCADE, null=True, related_name="+"
    )
    thing = models.ForeignKey(SoftDeletedModel, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=100, blank=True)
    text2 = models.CharField(max_length=100, blank=True)
    deleted = models.BooleanField(default=False)
    safe = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UnchangeableModel(models.Model):
    pass
