from django.contrib import admin
from industries.models import Industries
# Register your models here.


@admin.register(Industries)
class IndustriesAdmin(admin.ModelAdmin):
    list_display = [
            "id",
            "name",
            "is_default",
            "status",
            "created_at",
            "updated_at",
        ]