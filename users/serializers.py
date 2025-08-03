from rest_framework import serializers #Medium+Dev.to+Cgpt
from .models import User
#from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

def validate_password(value):
    if len(value) < 8:
        raise serializers.ValidationError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in value):
        raise serializers.ValidationError("Password must contain at least one digit.")
    if not any(char.isalpha() for char in value):
        raise serializers.ValidationError("Password must contain at least one letter.")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in value):
        raise serializers.ValidationError("Password must contain at least one special character.")
    return value
    
class RegisterSerializer(serializers.Serializer):
    id=serializers.UUIDField(read_only=True)
    email=serializers.EmailField()
    username=serializers.CharField()
    password = serializers.CharField(write_only=True, validators=[validate_password])
    role= serializers.ChoiceField(choices=User.ROLE_CHOICES, default='staff')
    def create(self, validated_data):
        role=validated_data.pop('role','staff')
        password=validated_data.pop('password')
        user=User(**validated_data)
        user.set_password(password)
        user.role=role
        user.save()
        return user
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value
class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    def validate(self,data):
        user=authenticate(email=data['email'],password=data['password'])
        if not user:
            raise serializers.ValidationError("Incorrect Credentials")
        data['user']=user
        return data

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    email = serializers.EmailField()
    username = serializers.CharField()
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, read_only=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance

    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, validators=[validate_password])