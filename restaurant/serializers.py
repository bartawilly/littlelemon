from rest_framework import serializers
from .models import Menu
from .models import Booking
from .models import MenuItem
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    class Meta:
        model = User
        fields = ['url', 'username','password', 'email', 'groups']
        
    def create(self, validated_data):
        user = User(
            email=validated_data.get('email', None),
            username=validated_data.get('username', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'