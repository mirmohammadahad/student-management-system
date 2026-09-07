from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enrollment
from .forms import EnrollmentForm

# ১. এনরোলমেন্টের তালিকা প্রদর্শন
def enrollment_list(request):
    # N+1 Query রোধ করতে select_related ব্যবহার করা হয়েছে
    enrollments = Enrollment.objects.select_related('student', 'course').all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

# ২. নতুন এনরোলমেন্ট তৈরি
def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_dict():
            form.save()
            return redirect('enrollments:enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollments/enrollment_form.html', {'form': form})

# ৩. এনরোলমেন্ট আপডেট করা
def enrollment_update(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollments:enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'enrollments/enrollment_form.html', {'form': form, 'enrollment': enrollment})

# ৪. এনরোলমেন্ট মুছে ফেলা
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollments:enrollment_list')
    return render(request, 'enrollments/enrollment_confirm_delete.html', {'enrollment': enrollment})