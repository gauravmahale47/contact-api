from django.db import models
import uuid


class Industries(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256, null=False, blank=False)
    is_default = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'industries'
        managed = True
        verbose_name = 'industry'
        verbose_name_plural = 'industries'
