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
        return render(request, "income_create.html", {"users":users, 'category':category})
    elif request.method == "POST":
        amount = request.POST.get('amount', False)
        description = request.POST.get('description', False)
        category_id = request.POST.get('category', False)
        if not amount or not description or not category_id:
            return render(request, "income_create.html", {
                'amount':amount,
                'description':description,
                'users': User.objects.all(),
                'category': Category.objects.all()
            })
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return HttpResponse("Категория не найдена")
        Income.objects.create(
            amount = amount,
            description = description,
            user = request.user,
            category = category,
        )
        return redirect("income_list")    
    



def incomes_edit_view(request, pk):
    income = Income.objects.filter(id = pk).first()
    users = User.objects.all()
    categories = Category.objects.all()
    if not income:
        return HttpResponse('Income not found')
    if request.method == "GET":
        return render(request, "income_edit.html", {'income':income, 'users':users, 'category': categories,})
    elif request.method == "POST":
        amount = request.POST.get('amount', False)
        description = request.POST.get('description', False)
        category_id = request.POST.get('category')
        if not amount or not description or not category_id:
            return render(request, "income_edit.html", {
                'income': income,
                'amount': amount,
                'description': description,
                'users': users,
                'category': categories,
            })
        # user = User.objects.filter(id=user_id).first()
        if not request.user.is_authenticated:
            return HttpResponse("User not found")
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return HttpResponse("Категория не найдена")
        income.amount = amount
        income.description = description
        income.category = category 
        income.user = request.user
        income.save()
        return redirect('income_list')


def income_delete_view(request, pk):
    income = Income.objects.filter( id = pk).first()
    if not income:
        return HttpResponse("Income not found")
    if request.method == "GET":
        return render(request, "income_delete.html", {'income':income})
    elif request.method == "POST":
        income.delete()
        return  redirect("income_list")






def expense_list_view(request):
    if request.method == 'GET':
        expenses = Expense.objects.filter(user=request.user).order_by("-id")
        return render(request, "expense_list.html", {"expenses":expenses})

    

def expense_create_view(request):
    categories = Category.objects.all()
    if request.method == "GET":
        users = User.objects.all()
        return render(request, "expense_create.html", {"users":users, 'categories':categories})
    elif request.method == "POST":
        amount = request.POST.get('amount', False)
        description = request.POST.get('description', False)
        category_id = request.POST.get('category', False)
        if not amount or not description or not category_id:
            return render(request, "expense_create.html", {
                'amount':amount,
                'description':description,
                'users': User.objects.all(),
                'categories': categories,
            })
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return HttpResponse("Категория не найдена")
        Expense.objects.create(
            amount = amount,
            description = description,
            user = request.user,
            category = category,
        )
        return redirect("expense_list")    
    



def expense_edit_view(request, pk):
    expense = Expense.objects.filter(id = pk).first()
    users = User.objects.all()
    categories = Category.objects.all()
    if not expense:
        return HttpResponse('Expense not found')
    if request.method == "GET":
        return render(request, "expense_edit.html", {'expense':expense, 'users':users, 'categories': categories})
    elif request.method == "POST":
        amount = request.POST.get('amount', False)
        description = request.POST.get('description', False)
        category_id = request.POST.get('category')
        if not amount or not description or not category_id:
            return render(request, "expense_edit.html", {
                'expense': expense,
                'amount': amount,
                'description': description,
                'users': users,
                'categories': categories
            })
        if not request.user.is_authenticated:
            return HttpResponse("User not found")
        category = Category.objects.filter(id=category_id).first()
        if not category:
            return HttpResponse("Категория не найдена")
        expense.amount = amount
        expense.description = description
        expense.category = category 
        expense.user = request.user
        expense.save()
        return redirect('expense_list')


def expense_delete_view(request, pk):
    expense = Expense.objects.filter(id=pk).first()
    if not expense:
        return HttpResponse("Expense not found")
    if request.method == "GET":
        return render(request, "expense_delete.html", {'expense':expense})
    elif request.method == "POST":
        expense.delete()
        return  redirect("expense_list")
