from rest_framework import serializers
from .models import BinStatus

class BinStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinStatus
        fields = ["id", "bio_status", "non_bio_status", "updated_at"]
