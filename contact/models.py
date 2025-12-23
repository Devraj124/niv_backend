from django.db import models

class ContactSubmission(models.Model):

    WEBSITE_CHOICES = (
        ('NIVIT', 'NIVIT'),
        ('NIVMASS', 'NIVMASS'),
        ('NIVBRM', 'NIVBRM'),
    )

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()

    source_website = models.CharField(
        max_length=20,
        choices=WEBSITE_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_website} - {self.full_name}"
