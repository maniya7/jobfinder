from django.shortcuts import render

from datetime import timedelta
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job


class DeactivateOldJobsAPIView(APIView):
    def post(self, request):
        one_day_ago = timezone.now() - timedelta(days=1)

        updated = Job.objects.filter(
            created_at__lt=one_day_ago,
            is_active=True
        ).update(is_active=False)

        return Response({
            "message": "Old jobs deactivated successfully",
            "updated_count": updated
        })
