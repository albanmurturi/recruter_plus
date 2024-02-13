from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='interview'),
    path('<int:id>/', views.interview_detail, name='interview_detail'),
]