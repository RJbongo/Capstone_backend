from django.db import models

class BinStatus(models.Model):
    STATUS_CHOICES = [
        ('not full', 'Not Full'),
        ('full', 'Full'),
    ]

    bio_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not full')
    non_bio_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not full')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bio: {self.bio_status}, Non-Bio: {self.non_bio_status} (updated {self.updated_at})"
