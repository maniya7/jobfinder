from django.urls import path
from .views import DeactivateOldJobsAPIView

urlpatterns = [
    path(
        'deactivate-old-jobs/',
        DeactivateOldJobsAPIView.as_view(),
        name='deactivate-old-jobs'
    ),
]