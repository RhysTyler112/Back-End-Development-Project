from django.shortcuts import render
from django.views import generic
from .models import GymClass

# Create your views here.
class ClassesList(generic.ListView):
    queryset = GymClass.objects.all()
    template_name = "Classes/classes_list.html"
    context_object_name = 'gym_classes'