from django.contrib import admin
from .models import Student, Department

admin.site.register(Department)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # আপনার Student মডেলে আসল ফিল্ডের নাম অনুযায়ী সাজানো হলো
    list_display = ('student_id', 'email', 'phone')
    search_fields = ('student_id', 'email', 'phone')