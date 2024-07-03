from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"