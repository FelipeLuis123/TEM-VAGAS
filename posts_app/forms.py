
from django import forms
from .models import recomendacoes
from .models import Comentario
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


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
        
        
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class UserProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password']



