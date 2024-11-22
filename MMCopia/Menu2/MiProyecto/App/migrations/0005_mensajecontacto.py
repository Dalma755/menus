# Generated by Django 5.1.2 on 2024-11-11 16:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_mesa_sector_pedido_adicional_bebida_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
                ('fecha_envio', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]