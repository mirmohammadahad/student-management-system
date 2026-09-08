from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Enrollment
from .forms import EnrollmentForm
from students.models import Student
from courses.models import Course

# ১. Dashboard View
@login_required
def dashboard(request):
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()
    recent_enrollments = Enrollment.objects.select_related('student', 'course').order_by('-enrollment_date')[:5]

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_enrollments': total_enrollments,
        'recent_enrollments': recent_enrollments,
    }
    return render(request, 'dashboard.html', context)

# ২. List View
@login_required
def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'course').all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

# ৩. Ledger + Pagination View
@login_required
def enrollment_ledger(request):
    enrollments = Enrollment.objects.select_related('student', 'course').all()

    search_query = request.GET.get('search', '')
    if search_query:
        enrollments = enrollments.filter(
            Q(student__student_id__icontains=search_query) |
            Q(student__email__icontains=search_query) |
            Q(course__code__icontains=search_query) |
            Q(course__title__icontains=search_query)
        )

    status_filter = request.GET.get('status', '')
    if status_filter:
        enrollments = enrollments.filter(status=status_filter)

    paginator = Paginator(enrollments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
    }
    return render(request, 'enrollments/ledger.html', context)

# ৪. Create View
@login_required
def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollments:enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollments/enrollment_form.html', {'form': form})

# ৫. Update View
@login_required
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

# ৬. Delete View
@login_required
def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollments:enrollment_list')
    return render(request, 'enrollments/enrollment_confirm_delete.html', {'enrollment': enrollment})

# ৭. AJAX Status Update API
@login_required
def update_enrollment_status_ajax(request, pk):
    if request.method == 'POST':
        enrollment = get_object_or_404(Enrollment, pk=pk)
        new_status = request.POST.get('status')
        if new_status in ['PENDING', 'APPROVED', 'CANCELLED']:
            enrollment.status = new_status
            enrollment.save()
            return JsonResponse({'success': True, 'new_status': enrollment.status})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

# ৮. Live Search API
@login_required
def live_search_enrollments(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        enrollments = Enrollment.objects.select_related('student', 'course').filter(
            Q(student__student_id__icontains=query) |
            Q(student__email__icontains=query) |
            Q(course__code__icontains=query) |
            Q(course__title__icontains=query)
        )[:5]

        for item in enrollments:
            results.append({
                'student_id': item.student.student_id,
                'student_email': item.student.email,
                'course_code': item.course.code,
                'status': item.status
            })
    return JsonResponse({'results': results})