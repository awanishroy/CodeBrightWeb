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
    PR_BOARD_id = serializers.IntegerField(write_only=True, required=True)
    PR_CLASSES = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=True
    )

    class Meta:
        model = CbtSeries
        fields = ['PR_SERIES_ID', 'PR_SERIES_NAME', 'PR_BOARD_id', 'PR_CLASSES', 'PR_CREATED_AT', 'PR_MODIFIED_AT']
        read_only_fields = ['PR_CREATED_AT', 'PR_MODIFIED_AT']  # Timestamps as read-only

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

    PR_TITLE = serializers.CharField(required=True)    
    PR_AUTHOR_id = serializers.IntegerField(required=True)
    PR_EDITION_id = serializers.IntegerField(required=True)
    PR_IMPRINT_id = serializers.IntegerField(required=True)
    PR_SERIES_id = serializers.IntegerField(required=True)

    class Meta:
        model = CbtBookData
        fields = '__all__'
