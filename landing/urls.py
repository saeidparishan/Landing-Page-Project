from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('landing.api.v1.urls')),
]
