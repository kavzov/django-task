from django.contrib.postgres.fields import JSONField
from django.db import models


class Field(models.Model):
    field_data = JSONField()

    def __str__(self):
    	return str(self.field_data)