from django.db import models
from django.dispatch import receiver
from accounts.models import CustomUser
from django.db.models.signals import post_save

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
    quantidade_banheiros = models.IntegerField()
    descricao = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    create_at = models.DateTimeField(auto_now_add=True) 
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)
    curtidas = models.ManyToManyField(CustomUser, through='Curtida', related_name='curtidas')
    
    def _str_(self):
        return self.nome
    
    
    class Meta:
        verbose_name = 'Imovel'
        verbose_name_plural = 'Imoveis'
        ordering = ['id']

class Curtida(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recomendacao = models.ForeignKey(recomendacoes, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'Curtida de {self.usuario.username} em {self.recomendacao.nome}'

class Myprofile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100)

@receiver(post_save, sender=CustomUser)
def my_handler(sender, **kwargs):
    if kwargs.get('created', False):
        Myprofile.objects.create(user=kwargs['instance'])
       
@receiver(post_save, sender=recomendacoes)
def create_curtida_on_recomendacao_creation(sender, instance, created, **kwargs):
    if created:
        Curtida.objects.create(usuario=instance.owner, recomendacao=instance)