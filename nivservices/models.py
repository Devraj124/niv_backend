from django.db import models
from ckeditor.fields import RichTextField


# =========================
# CONSTANTS
# =========================
WEBSITE_CHOICES = (
    ("NIVIT", "NIVIT"),
    ("NIVMASS", "NIVMASS"),
    ("NIVBRM", "NIVBRM"),
    ("NIVPAP", "NIVPAP"),
)


# =========================
# WEBSITE POLICY (SINGLE TABLE)
# =========================
class WebsitePolicy(models.Model):
    POLICY_TYPE_CHOICES = (
        ("TERMS", "Terms of Services"),
        ("PRIVACY", "Privacy Policy"),
        ("RETURN_REFUND", "Return & Refund Policy"),
        ("SHIPMENT", "Shipment Policy"),
    )

    website = models.CharField(
        max_length=20,
        choices=WEBSITE_CHOICES,
    )
    policy_type = models.CharField(
        max_length=30,
        choices=POLICY_TYPE_CHOICES,
    )

    title = models.CharField(max_length=255)
    content = RichTextField()

    class Meta:
        unique_together = ("website", "policy_type")
        verbose_name = "Website Policy"
        verbose_name_plural = "Website Policies"

    def __str__(self):
        return f"{self.website} – {self.policy_type}"


# ==================================================
# POLICY PROXIES (ADMIN DISPLAY ONLY)
# ==================================================
class NIVITTerms(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVIT – Terms of Services"
        verbose_name_plural = "NIVIT – Terms of Services"


class NIVMASSTerms(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVMASS – Terms of Services"
        verbose_name_plural = "NIVMASS – Terms of Services"


class NIVBRMTerms(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVBRM – Terms of Services"
        verbose_name_plural = "NIVBRM – Terms of Services"


class NIVPAPTerms(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVPAP – Terms of Services"
        verbose_name_plural = "NIVPAP – Terms of Services"


class NIVITPrivacy(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVIT – Privacy Policy"
        verbose_name_plural = "NIVIT – Privacy Policy"


class NIVMASSPrivacy(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVMASS – Privacy Policy"
        verbose_name_plural = "NIVMASS – Privacy Policy"


class NIVBRMPrivacy(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVBRM – Privacy Policy"
        verbose_name_plural = "NIVBRM – Privacy Policy"


class NIVPAPPrivacy(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVPAP – Privacy Policy"
        verbose_name_plural = "NIVPAP – Privacy Policy"


class NIVPAPReturnRefund(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVPAP – Return & Refund Policy"
        verbose_name_plural = "NIVPAP – Return & Refund Policy"


class NIVPAPShipment(WebsitePolicy):
    class Meta:
        proxy = True
        verbose_name = "NIVPAP – Shipment Policy"
        verbose_name_plural = "NIVPAP – Shipment Policy"


# =========================
# KNOWLEDGE BASE (WEBSITE-WISE)
# =========================
class KnowledgeBase(models.Model):
    website = models.CharField(
        max_length=20,
        choices=WEBSITE_CHOICES,
    )

    class Meta:
        verbose_name = "Knowledge Base"
        verbose_name_plural = "Knowledge Bases"

    def __str__(self):
        return f"{self.website} – Knowledge Base"


class KnowledgeBaseFile(models.Model):
    knowledgebase = models.ForeignKey(
        KnowledgeBase,
        related_name="files",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="knowledgebase/")

    class Meta:
        verbose_name = "Knowledge Base File"
        verbose_name_plural = "Knowledge Base Files"

    def __str__(self):
        return self.title


# =========================
# SOPs (WEBSITE-WISE)
# =========================
class SOP(models.Model):
    website = models.CharField(
        max_length=20,
        choices=WEBSITE_CHOICES,
    )

    class Meta:
        verbose_name = "SOP"
        verbose_name_plural = "SOPs"

    def __str__(self):
        return f"{self.website} – SOPs"


class SOPFile(models.Model):
    sop = models.ForeignKey(
        SOP,
        related_name="files",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="sops/")

    class Meta:
        verbose_name = "SOP File"
        verbose_name_plural = "SOP Files"

    def __str__(self):
        return self.title
