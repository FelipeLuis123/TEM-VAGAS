from django import forms
from .models import recomendacoes

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = recomendacoes # nosso modelo
        fields = '__all__'

    def __init__(self, *args, **kwargs): # Adiciona 
            super().__init__(*args, **kwargs)  
            for field_name, field in self.fields.items():   
                field.widget.attrs['class'] = 'form-control'        