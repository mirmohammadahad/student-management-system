from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student

# ১. সব স্টুডেন্ট দেখার ভিউ
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# ২. নতুন স্টুডেন্ট যোগ করার ভিউ
@login_required
def student_create(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Student.objects.create(
            student_id=student_id,
            email=email,
            phone=phone
        )
        return redirect('students:student_list')
    
    return render(request, 'students/student_form.html')

# ৩. স্টুডেন্টের তথ্য এডিট করার ভিউ
@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.student_id = request.POST.get('student_id')
        student.email = request.POST.get('email')
        student.phone = request.POST.get('phone')
        student.save()
        return redirect('students:student_list')

    return render(request, 'students/student_form.html', {'student': student})

# ৪. স্টুডেন্ট ডিলিট করার ভিউ
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:student_list')
        
    return render(request, 'students/student_confirm_delete.html', {'student': student})