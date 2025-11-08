from rest_framework import serializers
import re

class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=20)

    def validate_phone(self, value):
        # regex بین‌المللی برای شماره موبایل (مثلاً +989123456789)
        if not re.match(r'^\+?\d{10,15}$', value):
            raise serializers.ValidationError("شماره موبایل معتبر نیست.")
        return value
