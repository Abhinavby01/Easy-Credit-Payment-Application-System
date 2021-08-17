from rest_framework import serializers
from .models import customer,statements

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

class statementSerializer(serializers.ModelSerializer):
    class Meta:
        model = statements
        fields = ["statementPageOne", "statementPageTwo", "statementPageThree"]