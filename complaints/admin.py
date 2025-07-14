from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date_reported')
    list_filter = ('category', 'date_reported')
    search_fields = ('name', 'description', 'category')
    ordering = ('-date_reported',)
