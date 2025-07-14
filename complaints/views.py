import json
from django.shortcuts import render
from django.db.models import Count
from .models import Complaint

def dashboard(request):
    complaints = Complaint.objects.all().order_by('-date_reported')

    complaint_counts = Complaint.objects.values('category').annotate(count=Count('category'))
    labels = [entry['category'].capitalize() for entry in complaint_counts]
    data = [entry['count'] for entry in complaint_counts]

    context = {
        'complaints': complaints,
        'labels': json.dumps(labels),
        'data': json.dumps(data)
    }
    return render(request, 'complaints/dashboard.html', context)
