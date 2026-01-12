from rest_framework import serializers
from .models import (
    WebsitePolicy,
    KnowledgeBaseFile,
    SOPFile,
)


# ==================================================
# WEBSITE POLICIES SERIALIZER
# ==================================================
class WebsitePolicySerializer(serializers.ModelSerializer):
    """
    Used for:
    - Terms of Services
    - Privacy Policy
    - Return & Refund Policy
    - Shipment Policy
    """

    class Meta:
        model = WebsitePolicy
        fields = (
            "title",
            "content",
        )


# ==================================================
# KNOWLEDGE BASE FILE SERIALIZER
# ==================================================
class KnowledgeBaseFileSerializer(serializers.ModelSerializer):
    """
    Returns individual Knowledge Base PDF files
    """

    pdf = serializers.FileField(
        use_url=True,
        read_only=True,
    )

    class Meta:
        model = KnowledgeBaseFile
        fields = (
            "title",
            "pdf",
        )


# ==================================================
# SOP FILE SERIALIZER
# ==================================================
class SOPFileSerializer(serializers.ModelSerializer):
    """
    Returns individual SOP PDF files
    """

    pdf = serializers.FileField(
        use_url=True,
        read_only=True,
    )

    class Meta:
        model = SOPFile
        fields = (
            "title",
            "pdf",
        )
