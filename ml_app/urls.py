from django.urls import path
from .views import HelloWorldView, PredictionListView, PredictionRetrieveView, PredictionCreateView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('prediction/', PredictionListView.as_view(), name='predictions_list'),
    path('prediction/<int:pk>/', PredictionRetrieveView.as_view(), name='predictions_retrieve'),
    path('prediction/create/', PredictionCreateView.as_view(), name='predictions_create'),
]