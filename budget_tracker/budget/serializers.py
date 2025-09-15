#Convert data to and from JSON format
from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'name', 'amount', 'start_date', 'end_date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Automatically set the user from the request
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
