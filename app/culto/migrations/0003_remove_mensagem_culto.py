# Generated by Django 5.1.4 on 2024-12-25 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('culto', '0002_remove_mensagem_texto_mensagem_capitulo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='culto',
        ),
    ]
