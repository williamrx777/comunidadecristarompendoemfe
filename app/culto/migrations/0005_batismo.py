# Generated by Django 5.1.4 on 2024-12-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culto', '0004_culto_imagem_delete_galeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('local', models.CharField(max_length=255)),
                ('imagem', models.ImageField(default='', upload_to='batismo')),
            ],
        ),
    ]