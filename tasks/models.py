from django.db import models
from django.utils import timezone # Para usar a data/hora atual

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        # Ordena as tarefas por data de criação decrescente por padrão 
        # (as mais recentes aparecem primeiro)
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
