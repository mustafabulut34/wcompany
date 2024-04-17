import re

from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']

    def validate_phone_number(self, value):
        pattern = r"^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Geçersiz telefon numarası formatı.")
        return value
