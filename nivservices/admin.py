from django.contrib import admin
from .models import (
    # TERMS
    NIVITTerms, NIVMASSTerms, NIVBRMTerms,

    # PRIVACY
    NIVITPrivacy, NIVMASSPrivacy, NIVBRMPrivacy,

    # KNOWLEDGE BASE
    NIVITKnowledgeBase, NIVMASSKnowledgeBase, NIVBRMKnowledgeBase,
    KnowledgeBaseFile,

    # SOPs
    NIVITSOP, NIVMASSSOP, NIVBRMSOP,
    SOPFile,
)


# =====================================================
# BASE WEBSITE ADMIN (AUTO WEBSITE + HIDE FIELD)
# =====================================================
class BaseWebsiteAdmin(admin.ModelAdmin):
    website = None
    exclude = ("website",)   # 🔥 Website field hidden everywhere

    def get_queryset(self, request):
        return super().get_queryset(request).filter(website=self.website)

    def save_model(self, request, obj, form, change):
        obj.website = self.website
        super().save_model(request, obj, form, change)


# =====================================================
# TERMS / PRIVACY BASE
# =====================================================
class BasePolicyAdmin(BaseWebsiteAdmin):
    fields = ("title", "content")
    policy_type = None

    def get_queryset(self, request):
        return super().get_queryset(request).filter(policy_type=self.policy_type)

    def save_model(self, request, obj, form, change):
        obj.policy_type = self.policy_type
        super().save_model(request, obj, form, change)


# ================= TERMS =================
@admin.register(NIVITTerms)
class NIVITTermsAdmin(BasePolicyAdmin):
    website = "NIVIT"
    policy_type = "TERMS"


@admin.register(NIVMASSTerms)
class NIVMASSTermsAdmin(BasePolicyAdmin):
    website = "NIVMASS"
    policy_type = "TERMS"


@admin.register(NIVBRMTerms)
class NIVBRMTermsAdmin(BasePolicyAdmin):
    website = "NIVBRM"
    policy_type = "TERMS"


# ================= PRIVACY =================
@admin.register(NIVITPrivacy)
class NIVITPrivacyAdmin(BasePolicyAdmin):
    website = "NIVIT"
    policy_type = "PRIVACY"


@admin.register(NIVMASSPrivacy)
class NIVMASSPrivacyAdmin(BasePolicyAdmin):
    website = "NIVMASS"
    policy_type = "PRIVACY"


@admin.register(NIVBRMPrivacy)
class NIVBRMPrivacyAdmin(BasePolicyAdmin):
    website = "NIVBRM"
    policy_type = "PRIVACY"


# =====================================================
# KNOWLEDGE BASE (ONLY INLINE TITLE + PDF)
# =====================================================
class KnowledgeBaseFileInline(admin.TabularInline):
    model = KnowledgeBaseFile
    extra = 1


@admin.register(NIVITKnowledgeBase)
class NIVITKnowledgeBaseAdmin(BaseWebsiteAdmin):
    website = "NIVIT"
    inlines = [KnowledgeBaseFileInline]
    fields = ()            # 🔥 NO parent title
    readonly_fields = ()


@admin.register(NIVMASSKnowledgeBase)
class NIVMASSKnowledgeBaseAdmin(NIVITKnowledgeBaseAdmin):
    website = "NIVMASS"


@admin.register(NIVBRMKnowledgeBase)
class NIVBRMKnowledgeBaseAdmin(NIVITKnowledgeBaseAdmin):
    website = "NIVBRM"


# =====================================================
# SOPs (ONLY INLINE TITLE + PDF)
# =====================================================
class SOPFileInline(admin.TabularInline):
    model = SOPFile
    extra = 1


@admin.register(NIVITSOP)
class NIVITSOPAdmin(BaseWebsiteAdmin):
    website = "NIVIT"
    inlines = [SOPFileInline]
    fields = ()            # 🔥 NO parent title
    readonly_fields = ()


@admin.register(NIVMASSSOP)
class NIVMASSSOPAdmin(NIVITSOPAdmin):
    website = "NIVMASS"


@admin.register(NIVBRMSOP)
class NIVBRMSOPAdmin(NIVITSOPAdmin):
    website = "NIVBRM"
