from rest_framework import viewsets, permissions
from .models import Expense, Category
from .serializers import ExpenseSerializer, CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return categories belonging to the logged-in user
        return Category.objects.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        # Auto-attach the user when creating a new category
        serializer.save(user=self.request.user)