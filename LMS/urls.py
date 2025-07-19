from django.urls import path
from .views import *

urlpatterns = [
    path("", incomes_list_view, name='income_list'),
    path("create/", incomes_create_view, name='income_create'),
    path('<int:pk>/', incomes_edit_view, name='income_edit'),
]