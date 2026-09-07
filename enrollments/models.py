from django.db import models

# Create your models here.
from django.db import models
from students.models import Student  # আপনার students অ্যাপের Student মডেল
from courses.models import Course

class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('CANCELLED', 'Cancelled'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='APPROVED')

    class Meta:
        unique_together = ('student', 'course') # একজন শিক্ষার্থী একই কোর্সে একাধিকবার এনরোলমেন্ট করতে পারবে না

    def __str__(self):
        return f"{self.student} - {self.course.code}"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('BKASH', 'bKash'),
        ('NAGAD', 'Nagad'),
        ('BANK', 'Bank Transfer'),
        ('CASH', 'Cash'),
    )

    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='BKASH')
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.amount} BDT"


class Ledger(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('DEBIT', 'Debit (Course Fee)'),
        ('CREDIT', 'Credit (Payment Received)'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='ledger_entries')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.transaction_type}: {self.amount}"