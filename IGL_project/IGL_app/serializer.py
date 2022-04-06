from rest_framework import serializers
from .models import IGL_account
from django.contrib.auth.models import User


class IGLRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = IGL_account
        fields = ('first_name', 'last_name', 'mobile_number', 'IGL_username', 'Email', 'password', 'confirm_password')
        extra_kwargs = {
            'password,': {'write_only': True},

        }

    def create(self, validated_data):
        user = IGL_account.objects.create(**validated_data)
        # user = IGL_account.objects.create(validated_data['IGL_username'], first_name=validated_data['first_name'],
        #                                 last_name=validated_data['last_name'], mobile_number=validated_data['mobile_number'],
        #                                           Email=validated_data['Email'],password=validated_data['password'],confirm_password=validated_data['confirm_password'])
        return user


# User serializer
class IGLUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IGL_account
        fields = '__all__'
