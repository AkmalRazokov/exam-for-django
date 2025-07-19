from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime



def incomes_list_view(request):
    if request.method == 'GET':
        incomes = Income.objects.filter(user=request.user).order_by("-id")
        return render(request, "income_list.html", {"incomes":incomes})

    


def incomes_create_view(request):
    if request.method == "GET":
        users = User.objects.all()
        category = Category.objects.all()
        return render(request, "income_create.html", {"users":users}, {'category':category})
    elif request.method == "POST":
        amount = request.POST.get('amount', False)
        description = request.POST.get('description', False)
        category_id = request.POST.get('category', False)
        if not amount or not description or not category_id:
            return render(request, "income_create.html", {
                'amount':amount,
                'description':description,
                'users': User.objects.all(),

            })
        Income.objects.create(
            amount = amount,
            description = description,
            user = request.user,
            category = request.category,
        )
        return redirect("income_list")    
    



def incomes_edit_view(request, pk):
    income = Income.objects.filter(id = pk).first()
    users = User.objects.all()
    if not income:
        return HttpResponse('Income not found')
    if request.method == "GET":
        return render(request, "income_edit.html", {'income':income, 'users':users})
    elif request.method == "POST":
        amount = request.POST.get('amount', False)
        description = request.POST.get('description', False)
        if not amount or not description:
            return render(request, "task_edit.html", {
                'amount':amount,
                'description':description,
            })
        # user = User.objects.filter(id=user_id).first()
        if not request.user.is_authenticated:
            return HttpResponse("User not found")
        income.amount = amount
        income.description = description
        income.category = income.category 
        income.user = request.user
        income.save()
        return redirect('income_list')


def task_delete_view(request, pk):
    income = Income.objects.filter( id = pk).first()
    if not income:
        return HttpResponse("Income not found")
    if request.method == "GET":
        return render(request, "income_delete.html", {'income':income})
    elif request.method == "POST":
        income.delete()
        return  redirect("income_list")
