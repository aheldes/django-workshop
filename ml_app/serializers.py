from rest_framework import serializers
from .models import Prediction
from .prediction_handler import Handler


class PredictionListSerializer(serializers.ModelSerializer):
    ocean_proximity = serializers.CharField(source='ocean_proximity.name')

    class Meta:
        model = Prediction
        fields = "__all__"


class PredictionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = [
            "longitude",
            "latitude",
            "housing_median_age",
            "total_rooms",
            "total_bedrooms",
            "population",
            "households",
            "median_income",
            "ocean_proximity",
        ]
    
    def create(self, validated_data):
        prediction_handler = Handler(validated_data)
        validated_data['price'] = round(prediction_handler.predict(), 2)
        return Prediction.objects.create(**validated_data)
