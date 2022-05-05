import re
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'BudgetApp/index.html')

def add_expense(request):
    return render(request, 'BudgetApp/add_expense.html')   
