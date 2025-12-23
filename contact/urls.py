from django.urls import path
from .views import (
    NIVITContactView,
    NIVMASSContactView,
    NIVBRMContactView
)

urlpatterns = [
    path('nivit/contact/', NIVITContactView.as_view()),
    path('nivmass/contact/', NIVMASSContactView.as_view()),
    path('nivbrm/contact/', NIVBRMContactView.as_view()),
]
