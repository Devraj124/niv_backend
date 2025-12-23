from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer


class NIVITContactView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['source_website'] = 'NIVIT'
        serializer = ContactSubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "NIVIT Contact Saved"}, status=201)
        return Response(serializer.errors, status=400)


class NIVMASSContactView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['source_website'] = 'NIVMASS'
        serializer = ContactSubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "NIVMASS Contact Saved"}, status=201)
        return Response(serializer.errors, status=400)


class NIVBRMContactView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['source_website'] = 'NIVBRM'
        serializer = ContactSubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "NIVBRM Contact Saved"}, status=201)
        return Response(serializer.errors, status=400)
