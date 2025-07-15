from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm
from django.db.models import Count

def dashboard(request):
    complaints = Complaint.objects.all().order_by('-date_reported')

    # Prepare data for chart
    complaint_counts = Complaint.objects.values('category').annotate(count=Count('category'))
    labels = [entry['category'].capitalize() for entry in complaint_counts]
    data = [entry['count'] for entry in complaint_counts]

    context = {
        'complaints': complaints,
        'labels': labels,
        'data': data
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
