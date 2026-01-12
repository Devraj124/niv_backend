from rest_framework import serializers
from .models import (
    WebsitePolicy,
    KnowledgeBase, KnowledgeBaseFile,
    SOP, SOPFile
)


# -------- POLICIES --------
class WebsitePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsitePolicy
        fields = ('title', 'content')


# -------- KNOWLEDGE BASE --------
class KnowledgeBaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeBaseFile
        fields = ('title', 'pdf')


class KnowledgeBaseSerializer(serializers.ModelSerializer):
    files = KnowledgeBaseFileSerializer(many=True)

    class Meta:
        model = KnowledgeBase
        fields = ('title', 'files')


# -------- SOPs --------
class SOPFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOPFile
        fields = ('title', 'pdf')


class SOPSerializer(serializers.ModelSerializer):
    files = SOPFileSerializer(many=True)

    class Meta:
        model = SOP
        fields = ('title', 'files')




# ================= POLICIES =================
class WebsitePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsitePolicy
        fields = ("title", "content")


# ================= KNOWLEDGE BASE =================
class KnowledgeBaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeBaseFile
        fields = ("title", "pdf")


# ================= SOPs =================
class SOPFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SOPFile
        fields = ("title", "pdf")
