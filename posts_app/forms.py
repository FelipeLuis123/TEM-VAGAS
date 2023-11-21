from django import forms
from .models import recomendacoes

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = recomendacoes
        exclude = ('owner', 'curtidas')
        
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'