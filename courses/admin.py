from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # আপনার Course মডেলের আসল ফিল্ড নাম: code, title, credit_hours, course_fee, is_active
    list_display = ('code', 'title', 'credit_hours', 'course_fee', 'is_active')
    search_fields = ('code', 'title')
    list_filter = ('is_active',)