from django.contrib import admin
from .models import Enrollment, Payment, Ledger

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    # আপনার Enrollment মডেলের ফিল্ড: student, course, status, enrollment_date
    list_display = ('student', 'course', 'status', 'enrollment_date')
    search_fields = ('student__student_id', 'course__code', 'course__title')
    list_filter = ('status', 'enrollment_date')
    raw_id_fields = ('student', 'course')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'enrollment', 'amount', 'payment_method', 'payment_date')

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ('student', 'transaction_type', 'amount', 'created_at')