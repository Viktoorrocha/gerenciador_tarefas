from django import forms 
from .models import Task 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['title', 'description', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da Tarefa'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descrição detalhada (opcional)'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'due_date': 'Data de Vencimento',
        }