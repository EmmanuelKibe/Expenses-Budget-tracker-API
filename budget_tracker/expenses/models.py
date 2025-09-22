from django.db import models

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='expenses')
    budget = models.ForeignKey('budget.Budget', on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.amount}"
