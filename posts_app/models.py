from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

class recomendacoes(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    tipo_imovel = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=15)
    estado = models.CharField(max_length=15)
    cep = models.CharField(max_length=8)
    valor_aluguel = models.CharField(max_length=10)
    quantidade_quartos = models.CharField(max_length=2)
    quantidade_banheiros = models.CharField(max_length=2)
    descricao = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    create_at = models.DateTimeField(auto_now_add=True) 
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    curtidas = models.ManyToManyField(get_user_model(), through='Curtida', related_name='curtidas')
    favoritos = models.ManyToManyField(get_user_model(), through='Favorito', related_name='favoritos')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Imovel'
        verbose_name_plural = 'Imoveis'
        ordering = ['id']

class Curtida(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recomendacao = models.ForeignKey(recomendacoes, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Curtida de {self.usuario.username} em {self.recomendacao.nome}'
    

class Myprofile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100)

@receiver(post_save, sender=get_user_model())
def my_handler(sender, **kwargs):
    if kwargs.get('created', False):
        Myprofile.objects.create(user=kwargs['instance'])
       
@receiver(post_save, sender=recomendacoes)
def create_curtida_on_recomendacao_creation(sender, instance, created, **kwargs):
    if created:
        Curtida.objects.create(usuario=instance.owner, recomendacao=instance)
        Favorito.objects.create(usuario=instance.owner, recomendacao=instance)

        
class Comentario(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recomendacao = models.ForeignKey(recomendacoes, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.usuario.username} em {self.recomendacao.nome}'

class Favorito(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recomendacao = models.ForeignKey(recomendacoes, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Favorito de {self.usuario.username} em {self.recomendacao.nome}'





