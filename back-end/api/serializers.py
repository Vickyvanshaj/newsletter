from rest_framework import serializers
from .models import Mail

class MailSerializer(serializers.Serializer):
    mail=serializers.EmailField(max_length=100)

    def create(self,validate_data):
        return Mail.objects.create(**validate_data)
        