from django.urls import path
from .views import *

urlpatterns = [
    path("", incomes_list_view, name='income_list'),
    path("create/", incomes_create_view, name='income_create'),
    path('<int:pk>/', incomes_edit_view, name='income_edit'),
    path('delete/<int:pk>/', income_delete_view, name='income_delete'),

    path('expenses/', expense_list_view, name='expense_list'),
    path('expenses/create/', expense_create_view, name='expense_create'),
    path('expenses/edit/<int:pk>/', expense_edit_view, name='expense_edit'),
    path('expenses/delete/<int:pk>/', expense_delete_view, name='expense_delete'),
]