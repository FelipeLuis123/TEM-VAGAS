
from django import forms
from .models import recomendacoes
from .models import Comentario

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = recomendacoes
        exclude = ("owner", "curtidas", "favoritos" )

    def __init__(self, *args, **kwargs):  # Corrigido aqui
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]
        
        




