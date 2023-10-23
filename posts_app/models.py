from django.db import models
from django.dispatch import receiver
from accounts.models import CustomUser
from django.db.models.signals import post_save

# Create your models here.
class recomendacoes(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField()
    tipo_imovel = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.IntegerField()
    valor_aluguel = models.IntegerField()
    quantidade_quartos = models.IntegerField()
    quantidade_banheiros = models.IntegerField()  # Use IntegerField for quantity fields
    descricao = models.TextField()  # "Descricao" should be lowercase "descricao"
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    create_at = models.DateTimeField(auto_now_add=True) 
    #disponivel
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nome  # retornando o nome para representação da string do objeto
    
    class Meta:
        verbose_name = 'Imovel'
        verbose_name_plural = 'Imoveis'
        ordering = ['id']

class Myprofile(models.Model):
    user = models.OneToOneField(CustomUser, 
						on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100)


@receiver(post_save, sender=CustomUser)
def my_handler(sender, **kwargs):
    """
    Quando Criar um usuário no Django, vai rodar essa função
    para criar uma instancia nesse modelo MyProfile no campo "user".
    """
    if kwargs.get('created', False):
        Myprofile.objects.create(user=kwargs['instance'])
       