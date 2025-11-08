from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('landing.api.v1.urls')),
]
