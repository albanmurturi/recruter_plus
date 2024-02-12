from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/<int:id>/', views.subject_detail, name='subject_detail'),
]
