import uuid
from django.db import models
from django.conf import settings

class Candidate(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='candidate'
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    birth_date = models.DateField(null=True,blank=True)

    gender = models.CharField(max_length=20,blank=True)

    address = models.TextField(blank=True)

    bio = models.TextField(blank=True)

    def __str__(self):
       return f'{self.first_name}{self.last_name}'



class Resume(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='resumes'
    )

    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    file = models.FileField(upload_to='resumes/', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title


class Experience(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='experiences'
    )

    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def str(self):
        return self.job_title


class Education(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='educations'
    )

    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=150)
    university = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(null=True, blank=True)

    def str(self):
        return self.university

class CandidateSkill(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='candidate_skills'
    )

    skill = models.ForeignKey(
        'jobs.Skill',
        on_delete=models.CASCADE,
        related_name='candidate_skills'
    )

    proficiency_level = models.CharField(max_length=50)
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['candidate', 'skill'],
                name='unique_candidate_skill'
            )
        ]

    def str(self):
        return f'{self.candidate} - {self.skill}'