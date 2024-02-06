from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include("feed.urls")),
    path('api-auth/', include('rest_framework.urls'))
]
