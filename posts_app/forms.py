from django import forms
from .models import recomendacoes

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = recomendacoes
        exclude = ['owner']  # Exclua o campo owner do formulário

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
     