from django.db import models
from django.contrib.auth.models import User


class EmailHistory(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="emails")
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_content = models.TextField(blank=True, null=True)

    category = models.CharField(max_length=50)  # PRODUTIVO / IMPRODUTIVO
    ai_response = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Histórico de Email"
        verbose_name_plural = "Histórico de Emails"
