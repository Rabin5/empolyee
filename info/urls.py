from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from info.models import Empolyee

from .views import (EmplyeeListCreateView, EmplyeeListView,
                    EmplyeeRetriveUpdateDestroyView, EmpolyeeCreateView,
                    EmpolyeeDeleteView, EmpolyeeDetailView, EmpolyeeUpdateView)

app_name = 'info'

urlpatterns = [
    # for api crud
    path('empolyee/', EmplyeeListCreateView.as_view(), name='emp_api'),
    path('empolyee/<int:pk>/', EmplyeeRetriveUpdateDestroyView.as_view()),

    # for model form crud  ,
    path('empolyee_crt/', EmpolyeeCreateView.as_view(), name='emp_cre'),
    path('empolyee_del/<int:pk>/', EmpolyeeDeleteView.as_view(), name='emp_det'),
    path('empolyee_det/<int:pk>/', EmpolyeeDetailView.as_view(), name='emp_del'),
    path('empolyee_up/<int:pk>/', EmpolyeeUpdateView.as_view(), name='emp_up'),
    path('', EmplyeeListView.as_view(), name='emp_list'),
]
