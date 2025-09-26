from django.urls import path
from .views import BudgetReportView

urlpatterns = [
    path("budgets/", BudgetReportView.as_view(), name="budget-report"),
]
