# Generated by Django 4.2.3 on 2023-11-21 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_app', '0003_recomendacoes_owner_alter_recomendacoes_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curtida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('recomendacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.recomendacoes')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recomendacoes',
            name='curtidas',
            field=models.ManyToManyField(related_name='curtidas', through='posts_app.Curtida', to=settings.AUTH_USER_MODEL),
        ),
    ]
