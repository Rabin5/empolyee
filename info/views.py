from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import *
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Empolyee
from .serializer import EmpolyeeSerializer
from .forms import EmpolyeeCreateForm, EmpolyeeUpdateForm
from django.urls import reverse_lazy


class EmplyeeListCreateView(ListCreateAPIView):
    queryset = Empolyee.objects.all()
    serializer_class = EmpolyeeSerializer


class EmplyeeRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Empolyee.objects.all()
    serializer_class = EmpolyeeSerializer


class EmplyeeListView(ListView):
    template_name = 'emp_list.html'
    model = Empolyee
    # paginate_by = 100  # if pagination is desired

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context


class EmpolyeeCreateView(CreateView):
    template_name = 'emp_create.html'
    models = Empolyee
    form_class = EmpolyeeCreateForm
    success_url = reverse_lazy('info:emp_list')


class EmpolyeeUpdateView(UpdateView):
    template_name = 'emp_update.html'
    model = Empolyee
    form_class = EmpolyeeUpdateForm
    success_url = reverse_lazy('info:emp_list')
    # form_class =


class EmpolyeeDetailView(DetailView):
    template_name = 'emp_detail.html'
    model = Empolyee


class EmpolyeeDeleteView(DeleteView):
    template_name = 'emp_delete.html'
    model = Empolyee
    success_url = reverse_lazy('info:emp_list')
