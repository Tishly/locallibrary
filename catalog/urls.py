from django.urls import path
from . import views

# Add static files to path
urlpatterns = [
    path('', views.index, name='index'),
]