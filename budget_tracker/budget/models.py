from django.db import models

# Create your models here.
class Budget(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.amount}" 
