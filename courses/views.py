from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

# ১. কোর্সের তালিকা প্রদর্শন
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# ২. নতুন কোর্স তৈরি
def course_create(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        title = request.POST.get('title')
        credit_hours = request.POST.get('credit_hours')
        course_fee = request.POST.get('course_fee')
        is_active = request.POST.get('is_active') == 'on'  # Checkbox হ্যান্ডেল করা

        Course.objects.create(
            code=code,
            title=title,
            credit_hours=credit_hours,
            course_fee=course_fee,
            is_active=is_active
        )
        return redirect('courses:course_list')

    return render(request, 'courses/course_form.html')

# ৩. কোর্স আপডেট করা
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        course.code = request.POST.get('code')
        course.title = request.POST.get('title')
        course.credit_hours = request.POST.get('credit_hours')
        course.course_fee = request.POST.get('course_fee')
        course.is_active = request.POST.get('is_active') == 'on'
        course.save()
        return redirect('courses:course_list')

    return render(request, 'courses/course_form.html', {'course': course})

# ৪. কোর্স মুছে ফেলা
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('courses:course_list')

    return render(request, 'courses/course_confirm_delete.html', {'course': course})