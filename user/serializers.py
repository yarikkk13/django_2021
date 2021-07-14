import datetime
from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=0, max_value=datetime.date.today().year)
    name = serializers.CharField(validators=[
        RegexValidator('^[a-zA-Z]{2,20}$', 'only alpha min 2ch max 20ch')
    ])

    class Meta:
        model = UserModel
        fields = '__all__'

    def validate_age(self, age):
        if age % 2 == 0:
            raise serializers.ValidationError('only odd years')
        return age

    def validate(self, attrs):
        print(attrs)
        return attrs
