from django.db import models

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('phishing', 'Phishing'),
        ('hacking', 'Hacking'),
        ('fraud', 'Online Fraud'),
        ('harassment', 'Cyber Harassment'),
        ('others', 'Others'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"
