from rest_framework import serializers
from . models import Profile
from django.contrib.auth.models import User

from . utils import SendMail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field =['username','email']

        class ProfileSerielizer(serializers.ModelSeriazer):
            class Meta:
                model = UserSerializer
                fields=['fullname','gender''phone','image']

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(Write_only=True)
    password2 = serializers.CharField(Write_only=True)
    username = serializers.CharField(Write_only=True)
    email = serializers.EmailField(Write_only=True)

    class Meta:
        model = Profile
        fields = ['fullname','username','email','password1','password2','gender','phone','image']

    def validate(self, data):
       if data ['password1'] != data ['password2']:
           raise serializers.ValidationError('password not match')
       return data
    
    def create (self, validated_data):
        username = validated_data.pop('username')
        email =validated_data.pop('email')
        password = validated_data.pop('password1')

        user = User.objects.create_user(username=username,email=email,password=password)

        profile = Profile.objects.create(
            user=user,
            fullname= validated_data['fullname'],
            phone= validated_data['phone'],
            gender= validated_data['gender'],
            image= validated_data.get['image'],
        )
        SendMail(email,profile.fullname)
        return profile
