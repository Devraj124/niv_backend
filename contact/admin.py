from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'email',
        'phone_number',
        'source_website',
        'created_at'
    )

    list_filter = ('source_website',)
    search_fields = ('full_name', 'email', 'phone_number', 'company_name')
    readonly_fields = ('created_at',)

    def get_queryset(self, request):
        return super().get_queryset(request)
