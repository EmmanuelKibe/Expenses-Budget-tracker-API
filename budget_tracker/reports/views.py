from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from budget.models import Budget
from expenses.models import Expense

class BudgetReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        budgets = Budget.objects.filter(user=user)
        report = []

        for budget in budgets:
            total_expenses = sum(exp.amount for exp in budget.expenses.all())
            report.append({
                "budget": budget.name,
                "budgeted_amount": budget.amount,
                "total_expenses": total_expenses,
                "remaining": budget.amount - total_expenses
            })

        return Response(report)
