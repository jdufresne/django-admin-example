from django.db import models


class ManyInstancesModel(models.Model):
    value1 = models.CharField(max_length=100, blank=True)
    value2 = models.CharField(max_length=100, blank=True)


class StackedModel(models.Model):
    parent = models.ForeignKey(ManyInstancesModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)


class TabularModel(models.Model):
    parent = models.ForeignKey(ManyInstancesModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, help_text="The model's text")


class ForeignKeyModel(models.Model):
    parent = models.ForeignKey(ManyInstancesModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, blank=True)
    text2 = models.CharField(max_length=100, blank=True)
    deleted = models.BooleanField(default=False)
    safe = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UnchangeableModel(models.Model):
    pass
