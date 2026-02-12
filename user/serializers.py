from rest_framework import serializers
from user.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'username', 'password')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            phone_number=validated_data['phone_number'],
            username=validated_data['username'],
        )

        return user



