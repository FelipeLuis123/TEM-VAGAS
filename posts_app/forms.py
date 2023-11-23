from django import forms
from .models import recomendacoes
from .models import Comentario


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = recomendacoes
        exclude = ("owner", "curtidas")

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]
