from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:id>/', views.list_details),
    path('<int:id>/delete', views.delete)
]