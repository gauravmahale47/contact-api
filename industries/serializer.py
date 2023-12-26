from rest_framework import serializers
from industries.models import Industries
import re
from loguru import logger


class IndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = [
            "id",
            "name",
            "is_default",
            "status",
            "created_at",
            "updated_at",
        ]

    def validate_name(self, value):
        pattern = r'^[a-zA-Z ]+$'

        if not re.match(pattern, value):
            raise serializers.ValidationError("Only alphabets and space is allowed")
        return value