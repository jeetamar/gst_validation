from django.urls import path
from .views import HomeView,ValidateGst

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('validate-gst/',ValidateGst.as_view(),name='validate-gst'),
]