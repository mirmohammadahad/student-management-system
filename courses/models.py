from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Course Title")
    code = models.CharField(max_length=20, unique=True, verbose_name="Course Code")
    description = models.TextField(blank=True, null=True)
    credit_hours = models.PositiveIntegerField(default=3)
    course_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.title}"