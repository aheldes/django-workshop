from .models import Prediction
from .serializers import PredictionListSerializer, PredictionCreateSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
    
class PredictionListView(generics.ListAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionListSerializer


class PredictionRetrieveView(generics.RetrieveAPIView):
    queryset = Prediction.objects.all()
    serializer_class = PredictionListSerializer

class PredictionCreateView(APIView):
    
    def post(self, request):
        serializer = PredictionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        