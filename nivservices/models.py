from django.db import models
from ckeditor.fields import RichTextField


# =========================
# CONSTANTS
# =========================
WEBSITE_CHOICES = (
    ('NIVIT', 'NIVIT'),
    ('NIVMASS', 'NIVMASS'),
    ('NIVBRM', 'NIVBRM'),
)


# =========================
# WEBSITE POLICY
# =========================
class WebsitePolicy(models.Model):
    POLICY_TYPE_CHOICES = (
        ('TERMS', 'Terms of Services'),
        ('PRIVACY', 'Privacy Policy'),
    )

    website = models.CharField(max_length=20, choices=WEBSITE_CHOICES)
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPE_CHOICES)

    title = models.CharField(max_length=255)
    content = RichTextField()

    class Meta:
        unique_together = ('website', 'policy_type')

    def __str__(self):
        return f"{self.website} – {self.policy_type}"


# =========================
# TERMS (PROXY)
# =========================
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


# =========================
# PRIVACY (PROXY)
# =========================
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


# =========================
# KNOWLEDGE BASE (NO TITLE)
# =========================
class KnowledgeBase(models.Model):
    website = models.CharField(max_length=20, choices=WEBSITE_CHOICES)

    def __str__(self):
        return f"{self.website} – Knowledge Base"


class KnowledgeBaseFile(models.Model):
    knowledgebase = models.ForeignKey(
        KnowledgeBase,
        related_name="files",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="knowledgebase/")

    def __str__(self):
        return self.title


class NIVITKnowledgeBase(KnowledgeBase):
    class Meta:
        proxy = True
        verbose_name = "NIVIT – Knowledge Base"
        verbose_name_plural = "NIVIT – Knowledge Base"


class NIVMASSKnowledgeBase(KnowledgeBase):
    class Meta:
        proxy = True
        verbose_name = "NIVMASS – Knowledge Base"
        verbose_name_plural = "NIVMASS – Knowledge Base"


class NIVBRMKnowledgeBase(KnowledgeBase):
    class Meta:
        proxy = True
        verbose_name = "NIVBRM – Knowledge Base"
        verbose_name_plural = "NIVBRM – Knowledge Base"


# =========================
# SOPs (NO TITLE)
# =========================
class SOP(models.Model):
    website = models.CharField(max_length=20, choices=WEBSITE_CHOICES)

    def __str__(self):
        return f"{self.website} – SOPs"


class SOPFile(models.Model):
    sop = models.ForeignKey(
        SOP,
        related_name="files",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="sops/")

    def __str__(self):
        return self.title


class NIVITSOP(SOP):
    class Meta:
        proxy = True
        verbose_name = "NIVIT – SOPs"
        verbose_name_plural = "NIVIT – SOPs"


class NIVMASSSOP(SOP):
    class Meta:
        proxy = True
        verbose_name = "NIVMASS – SOPs"
        verbose_name_plural = "NIVMASS – SOPs"


class NIVBRMSOP(SOP):
    class Meta:
        proxy = True
        verbose_name = "NIVBRM – SOPs"
        verbose_name_plural = "NIVBRM – SOPs"
