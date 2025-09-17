from django.contrib import admin

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "amount", "date", "user", "budget")
    search_fields = ("name", "user__username", "budget__name")
    list_filter = ("date", "budget")
    ordering = ("-date",)

    