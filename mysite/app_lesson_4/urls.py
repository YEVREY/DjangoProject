from django.urls import path
from .views import index

urlpatterns = [
    path("lesson4/", index)
]
