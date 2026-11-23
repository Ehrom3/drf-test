from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class RegisterSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        
    def validate(self, attrs):
        if attrs ['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2':'Is not correct'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, role='client')
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()