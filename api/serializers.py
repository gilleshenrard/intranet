from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

    def save(self, **kwargs):
        """Ensures the password, if provided, is hashed before saving"""

        super(UserSerializer, self).save(**kwargs)

        if "password" in self.validated_data:
            self.instance.set_password(self.validated_data['password'])
            self.instance.save()

    def update(self, instance, validated_data):
        """Ensures the password, if provided, is hashed before updating"""

        super(UserSerializer, self).update(instance, validated_data)

        if "password" in self.validated_data:
            instance.set_password(self.validated_data['password'])
            instance.save()

        return instance
