
import uuid
from django.db import models


class Skill(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def str(self):
        return self.name


class Job(models.Model):

    class EmploymentType(models.TextChoices):
        FULL_TIME = 'full_time', 'تمام وقت'
        PART_TIME = 'part_time', 'پاره وقت'
        REMOTE = 'remote', 'دورکاری'
        CONTRACT = 'contract', 'قراردادی'

    class Status(models.TextChoices):
        DRAFT = 'draft', 'پیش نویس'
        ACTIVE = 'active', 'فعال'
        CLOSED = 'closed', 'بسته شده'
    is_active = models.BooleanField(default=True)

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    employer = models.ForeignKey(
        'companies.Employer',
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    employment_type = models.CharField(
        max_length=20,
        choices=EmploymentType.choices,
        default=EmploymentType.FULL_TIME
    )

    salary_min = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    salary_max = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    location = models.CharField(max_length=200)
    experience_required = models.PositiveIntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)

    def str(self):
        return self.title


class JobSkill(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='job_skills'
    )

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='job_skills'
    )

    is_required = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['job', 'skill'],
                name='unique_job_skill'
            )
        ]
    def str(self):
        return f'{self.candidate} - {self.job}'

class JobApplication(models.Model):

    class Status(models.TextChoices):
        PENDING = 'pending', 'در انتظار بررسی'
        REVIEWED = 'reviewed', 'بررسی شده'
        ACCEPTED = 'accepted', 'پذیرفته شده'
        REJECTED = 'rejected', 'رد شده'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    candidate = models.ForeignKey(
        'candidates.Candidate',
        on_delete=models.CASCADE,
        related_name='applications'
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    resume = models.ForeignKey(
        'candidates.Resume',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='applications'
    )

    cover_letter = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'applications_jobapplication'
        constraints = [
            models.UniqueConstraint(
                fields=['candidate', 'job'],
                name='unique_candidate_job_application'
            )
        ]

    def __str__(self):
        return f'{self.candidate} - {self.job}'

   
