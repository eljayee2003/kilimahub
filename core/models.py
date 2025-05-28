from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.core.validators import MinLengthValidator, MaxLengthValidator

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    country = models.CharField(max_length=2)
    is_verified = models.BooleanField(default=False)
    referral_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = "African User"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(
        max_length=160,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(160)
        ]
    )
    video_url = models.URLField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    search_vector = SearchVectorField(null=True)

    def clean(self):
        from core.utils.moderation import check_african_content
        check_african_content(self.content)

class Professional(models.Model):
    VERIFICATION_STATUS = [
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualifications = models.FileField(upload_to='qualifications/')
    verification_status = models.CharField(
        max_length=8,
        choices=VERIFICATION_STATUS,
        default='pending'
    )
    verified_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='verified_pros'
    )


# Create your models here.
