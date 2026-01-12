from django.contrib import admin
from .models import (
    # ================= POLICIES =================
    NIVITTerms, NIVMASSTerms, NIVBRMTerms,
    NIVITPrivacy, NIVMASSPrivacy, NIVBRMPrivacy,

    NIVPAPTerms, NIVPAPPrivacy,
    NIVPAPReturnRefund, NIVPAPShipment,

    # ================= KNOWLEDGE BASE =================
    KnowledgeBase,
    KnowledgeBaseFile,

    # ================= SOPs =================
    SOP,
    SOPFile,
)


# =====================================================
# BASE WEBSITE ADMIN
# =====================================================
class BaseWebsiteAdmin(admin.ModelAdmin):
    website = None
    exclude = ("website",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(website=self.website)

    def save_model(self, request, obj, form, change):
        obj.website = self.website
        super().save_model(request, obj, form, change)


# =====================================================
# BASE POLICY ADMIN
# =====================================================
class BasePolicyAdmin(BaseWebsiteAdmin):
    fields = ("title", "content")
    policy_type = None

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            policy_type=self.policy_type
        )

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


@admin.register(NIVPAPTerms)
class NIVPAPTermsAdmin(BasePolicyAdmin):
    website = "NIVPAP"
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


@admin.register(NIVPAPPrivacy)
class NIVPAPPrivacyAdmin(BasePolicyAdmin):
    website = "NIVPAP"
    policy_type = "PRIVACY"


# ================= RETURN / SHIPMENT (NIVPAP ONLY) =================
@admin.register(NIVPAPReturnRefund)
class NIVPAPReturnRefundAdmin(BasePolicyAdmin):
    website = "NIVPAP"
    policy_type = "RETURN_REFUND"


@admin.register(NIVPAPShipment)
class NIVPAPShipmentAdmin(BasePolicyAdmin):
    website = "NIVPAP"
    policy_type = "SHIPMENT"


# =====================================================
# KNOWLEDGE BASE (INLINE SAFE)
# =====================================================
class KnowledgeBaseFileInline(admin.TabularInline):
    model = KnowledgeBaseFile
    extra = 1


@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(BaseWebsiteAdmin):
    inlines = [KnowledgeBaseFileInline]
    fields = ()
    readonly_fields = ()


# =====================================================
# SOPs (INLINE SAFE)
# =====================================================
class SOPFileInline(admin.TabularInline):
    model = SOPFile
    extra = 1


@admin.register(SOP)
class SOPAdmin(BaseWebsiteAdmin):
    inlines = [SOPFileInline]
    fields = ()
    readonly_fields = ()
