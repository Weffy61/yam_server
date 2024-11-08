from django.contrib import admin
from django.urls import path

from yamarket_auth.views import authenticate_client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authenticate/', authenticate_client, name='authenticate_client'),
]
