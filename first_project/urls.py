from django.contrib import admin
from django.urls import path, include
from app.views import home_view


urlpatterns = [
    path('', home_view),
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
