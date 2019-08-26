from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Company, Favourite,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only':True,'required':True}}

    # def create(self,validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     token = Token.objects.create(user=user)
    #     return user

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','address','phone')

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favourite
        fields = ('id','mark','user','company')


