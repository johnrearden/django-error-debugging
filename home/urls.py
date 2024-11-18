from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('person/<int:pk>/', views.PersonDetail.as_view(), name='person_detail'),
]