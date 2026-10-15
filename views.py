from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'backend/dashboard.html')

def doctors(request):
    return render(request, 'backend/doctors.html')

def add_doctor(request):
    return render(request, 'backend/add_doctor.html')

def edit_doctor(request):
    return render(request, 'backend/edit_doctor.html')