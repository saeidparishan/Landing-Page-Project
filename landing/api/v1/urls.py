from django.urls import path
from .views import SubmitPhoneAPIView

urlpatterns = [
    path('submit-phone/', SubmitPhoneAPIView.as_view(), name='submit-phone'),
]
