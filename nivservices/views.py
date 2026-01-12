from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import (
    WebsitePolicy,
    KnowledgeBase,
    KnowledgeBaseFile,
    SOP,
    SOPFile
)

from .serializers import WebsitePolicySerializer


# ==================================================
# TERMS & PRIVACY POLICY API
# ==================================================
class PolicyAPIView(APIView):

    def get(self, request, website, policy_type):
        try:
            policy = WebsitePolicy.objects.get(
                website=website.upper(),
                policy_type=policy_type.upper()
            )
        except WebsitePolicy.DoesNotExist:
            return Response(
                {"error": "Policy not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(WebsitePolicySerializer(policy).data)


# ==================================================
# KNOWLEDGE BASE API (PDF LIST)
# ==================================================
class KnowledgeBaseAPIView(APIView):

    def get(self, request, website):
        kb = KnowledgeBase.objects.filter(
            website=website.upper()
        ).first()

        if not kb:
            return Response([], status=status.HTTP_200_OK)

        files = KnowledgeBaseFile.objects.filter(knowledgebase=kb)

        data = [
            {
                "title": file.title,
                "pdf": request.build_absolute_uri(file.pdf.url)
            }
            for file in files
        ]

        return Response(data, status=status.HTTP_200_OK)


# ==================================================
# SOPs API (PDF LIST)
# ==================================================
class SOPAPIView(APIView):

    def get(self, request, website):
        sop = SOP.objects.filter(
            website=website.upper()
        ).first()

        if not sop:
            return Response([], status=status.HTTP_200_OK)

        files = SOPFile.objects.filter(sop=sop)

        data = [
            {
                "title": file.title,
                "pdf": request.build_absolute_uri(file.pdf.url)
            }
            for file in files
        ]

        return Response(data, status=status.HTTP_200_OK)





# ==================================================
# TERMS / PRIVACY / RETURN / SHIPMENT
# ==================================================
class PolicyAPIView(APIView):
    """
    URL Example:
    /api/nivpap/terms/
    /api/nivpap/return_refund/
    """

    def get(self, request, website, policy_type):
        try:
            policy = WebsitePolicy.objects.get(
                website=website.upper(),
                policy_type=policy_type.upper()
            )
        except WebsitePolicy.DoesNotExist:
            return Response(
                {"error": "Policy not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            WebsitePolicySerializer(policy).data,
            status=status.HTTP_200_OK
        )


# ==================================================
# KNOWLEDGE BASE API
# ==================================================
class KnowledgeBaseAPIView(APIView):

    def get(self, request, website):
        kb = KnowledgeBase.objects.filter(
            website=website.upper()
        ).first()

        if not kb:
            return Response([], status=status.HTTP_200_OK)

        files = KnowledgeBaseFile.objects.filter(knowledgebase=kb)

        data = [
            {
                "title": file.title,
                "pdf": request.build_absolute_uri(file.pdf.url)
            }
            for file in files
        ]

        return Response(data, status=status.HTTP_200_OK)


# ==================================================
# SOP API
# ==================================================
class SOPAPIView(APIView):

    def get(self, request, website):
        sop = SOP.objects.filter(
            website=website.upper()
        ).first()

        if not sop:
            return Response([], status=status.HTTP_200_OK)

        files = SOPFile.objects.filter(sop=sop)

        data = [
            {
                "title": file.title,
                "pdf": request.build_absolute_uri(file.pdf.url)
            }
            for file in files
        ]

        return Response(data, status=status.HTTP_200_OK)