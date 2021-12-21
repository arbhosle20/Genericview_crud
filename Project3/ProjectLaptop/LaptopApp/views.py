from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Laptop


class LaptopCreateView(CreateView):
    model = Laptop
    fields = '__all__'
    success_url = '/cbv/list/'

class LaptopListView(ListView):
    model = Laptop


class LaptopUpdateView(UpdateView):
    model = Laptop
    fields = '__all__'
    success_url = '/cbv/list/'

class LaptopDeleteView(DeleteView):
    model = Laptop
    success_url='/cbv/list/'

# Create your views here.
