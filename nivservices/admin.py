from django.contrib import admin
from .models import (
    # ================= POLICIES (PROXY MODELS) =================
    NIVITTerms, NIVMASSTerms, NIVBRMTerms,
    NIVITPrivacy, NIVMASSPrivacy, NIVBRMPrivacy,
    NIVPAPTerms, NIVPAPPrivacy,
    NIVPAPReturnRefund, NIVPAPShipment,

    # ================= BASE MODELS =================
    WebsitePolicy,
    KnowledgeBase, KnowledgeBaseFile,
    SOP, SOPFile,
)


# =====================================================
# WEBSITE POLICY ADMIN (BASE – OPTIONAL)
# =====================================================
@admin.register(WebsitePolicy)
class WebsitePolicyAdmin(admin.ModelAdmin):
    list_display = ("website", "policy_type", "title")
    list_filter = ("website", "policy_type")
    search_fields = ("title",)
    fields = ("website", "policy_type", "title", "content")


# =====================================================
# POLICY ADMIN BASE (FOR PROXIES)
# =====================================================
class BasePolicyAdmin(admin.ModelAdmin):
    fields = ("title", "content")
    policy_type = None
    website = None

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(
            website=self.website,
            policy_type=self.policy_type,
        )

    def save_model(self, request, obj, form, change):
        obj.website = self.website
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


# ================= NIVPAP EXTRA POLICIES =================
@admin.register(NIVPAPReturnRefund)
class NIVPAPReturnRefundAdmin(BasePolicyAdmin):
    website = "NIVPAP"
    policy_type = "RETURN_REFUND"


@admin.register(NIVPAPShipment)
class NIVPAPShipmentAdmin(BasePolicyAdmin):
    website = "NIVPAP"
    policy_type = "SHIPMENT"


# =====================================================
# KNOWLEDGE BASE ADMIN (WEBSITE SELECT VISIBLE)
# =====================================================
class KnowledgeBaseFileInline(admin.TabularInline):
    model = KnowledgeBaseFile
    extra = 1


@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ("website",)
    list_filter = ("website",)
    fields = ("website",)           # 🔥 WEBSITE DROPDOWN VISIBLE
    inlines = [KnowledgeBaseFileInline]


# =====================================================
# SOP ADMIN (WEBSITE SELECT VISIBLE)
# =====================================================
class SOPFileInline(admin.TabularInline):
    model = SOPFile
    extra = 1


@admin.register(SOP)
class SOPAdmin(admin.ModelAdmin):
    list_display = ("website",)
    list_filter = ("website",)
    fields = ("website",)           # 🔥 WEBSITE DROPDOWN VISIBLE
    inlines = [SOPFileInline]
