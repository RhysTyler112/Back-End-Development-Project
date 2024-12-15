from . import views
from django.urls import path

urlpatterns = [
    path('', views.ClassesList.as_view(), name='home'),
]