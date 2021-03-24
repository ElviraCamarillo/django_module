
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import PetOwner, Pet
from .forms import OwnerForm, PetForm


# Create your views here.
class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"


class OwnersCreate(CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["owners"] = PetOwner.objects.all().orderby("created_at")
    #     print(context)
    #     return(context)



class OwnersUpdate(UpdateView):
    model = PetOwner
    form_class = OwnerForm
    template_name = 'vet/owners/update.html'
    success_url= reverse_lazy("vet:owners_list")

class PetsList(ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"


class PetsDetail(DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"

class PetsCreate(CreateView):
    model =  Pet
    template_name = 'vet/pets/create.html'
    form_class = PetForm 
    success_url = reverse_lazy('vet:pets_list')

    def get_initial(self):
        initial = {}
        for queryparam in self.request.GET:
            initial[queryparam] = self.request.GET[queryparam]
        return initial

class PetsUpdate(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'vet/pets/update.html'
    success_url= reverse_lazy("vet:pets_list")