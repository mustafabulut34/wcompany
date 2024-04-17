from django.db import models

from core.models import StarterModel
from users.models import User


class Store(StarterModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_url = models.URLField(unique=True)
    PLATFORM_CHOICES = [
        ('trendyol', 'Trendyol'),
        ('hepsiburada', 'Hepsiburada'),
        ('amazon', 'Amazon'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)

    def __str__(self):
        return f"{self.platform} - {self.store_url} | {self.user}"
