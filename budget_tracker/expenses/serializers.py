from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['user']  # User is set from the request context

        def validate(self, data):
            amount = data.get('amount')
            date = data.get('date')
            budget = data.get('budget')

            # 1. Check positive amount
            if amount <= 0:
                raise serializers.ValidationError("Expense amount must be greater than zero.")

            # 2. Check date within budget
            if date < budget.start_date or date > budget.end_date:
                raise serializers.ValidationError("Expense date must be within the budget period.")

            # 3. Prevent overspending
            total_expenses = sum(exp.amount for exp in budget.expenses.all())
            if total_expenses + amount > budget.amount:
                raise serializers.ValidationError("This expense exceeds the available budget.")

            return data
