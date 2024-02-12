from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Change 'some/path/' to your desired path
]
