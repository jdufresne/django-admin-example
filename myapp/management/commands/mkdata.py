import os
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from ... import models


class Command(BaseCommand):
    def handle(self, **options):
        User.objects.create_superuser(os.environ["USERNAME"], password="p")
        models.ManyInstancesModel.objects.bulk_create(
            [models.ManyInstancesModel() for _ in range(120)]
        )

        parent = models.ManyInstancesModel.objects.create()
        models.ForeignKeyModel.objects.create(parent=parent, text="child")

        parent = models.ManyInstancesModel.objects.create()
        models.ForeignKeyModel.objects.create(parent=parent)

        models.UnchangeableModel.objects.create()
