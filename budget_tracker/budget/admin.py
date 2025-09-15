# Register your models here.
from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):    
    list_display = ("id", "user", "name", "amount", "start_date", "end_date", "created_at", "updated_at")
    search_fields = ("name", "user__username", "user__email")
    list_filter = ("start_date", "end_date", "created_at", "updated_at")
    ordering = ("-created_at",)
