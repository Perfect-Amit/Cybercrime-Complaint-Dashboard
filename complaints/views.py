import json
from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Complaint
from .forms import ComplaintForm

def dashboard(request):
    complaints = Complaint.objects.all().order_by('-date_reported')

    # Aggregate chart data by category
    complaint_counts = Complaint.objects.values('category').annotate(count=Count('category'))
    labels = [entry['category'].capitalize() for entry in complaint_counts]
    data = [entry['count'] for entry in complaint_counts]

    context = {
        'complaints': complaints,
        'labels': json.dumps(labels),
        'data': json.dumps(data)
    }
    return render(request, 'complaints/dashboard.html', context)

def add_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ComplaintForm()
        
    return render(request, 'complaints/add_complaint.html', {'form': form})
