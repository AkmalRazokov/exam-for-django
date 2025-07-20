from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(User, related_name="user_incomes", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='category_income', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.amount} ({self.category.name})"

    
    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'


class Expense(models.Model):
    user = models.ForeignKey(User, related_name="user_expenses", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='expense_category', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return f"{self.user.username} {self.amount} ({self.category.name})"
        
    

