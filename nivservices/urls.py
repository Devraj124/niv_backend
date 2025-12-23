from django.urls import path
from .views import (
    PolicyAPIView,
    KnowledgeBaseAPIView,
    SOPAPIView
)

urlpatterns = [
    # 🔥 SPECIFIC ROUTES FIRST
    path('<str:website>/knowledgebase/', KnowledgeBaseAPIView.as_view()),
    path('<str:website>/sops/', SOPAPIView.as_view()),

    # 🔥 GENERIC ROUTE LAST
    path('<str:website>/<str:policy_type>/', PolicyAPIView.as_view()),
]
