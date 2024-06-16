from rest_framework import serializers

from settlements.models import Settlement


class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'