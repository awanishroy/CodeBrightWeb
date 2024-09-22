from rest_framework import serializers
from rest_framework.validators import *
from websiteApp.models import *

class CbtClassesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CbtClasses
        fields = '__all__'

class CbtBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtBoard
        fields = '__all__'

class CbtSeriesSerializer(serializers.ModelSerializer):

    PR_SERIES_NAME = serializers.CharField(required=True)    
    PR_CLASS_id = serializers.IntegerField(required=True)
    PR_BOARD_id = serializers.IntegerField(required=True)

    class Meta:
        model = CbtSeries
        fields = '__all__'

class CbtAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtAuthor
        fields = '__all__'

class CbtEditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtEdition
        fields = '__all__'

class CbtImprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtImprint
        fields = '__all__'

class CbtBookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtBookType
        fields = '__all__'

class CbtBookDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CbtBookData
        fields = '__all__'
