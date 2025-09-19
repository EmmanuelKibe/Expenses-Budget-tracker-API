from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    warning = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['user', 'warning']

    def validate(self, data):
        amount = data.get('amount')
        date = data.get('date')
        budget = data.get('budget')

        # 1. Positive amount check
        if amount <= 0:
            raise serializers.ValidationError("Expense amount must be greater than zero.")

        # 2. Date within budget
        if date < budget.start_date or date > budget.end_date:
            raise serializers.ValidationError("Expense date must be within the budget period.")

        return data

    # 3. Warning if budget exceeded
    def get_warning(self, obj):
        total_expenses = sum(exp.amount for exp in obj.budget.expenses.all())
        if total_expenses > obj.budget.amount:
            return "Warning: This budget has been exceeded."
        return None

