# Generated by Django 5.1.2 on 2024-10-28 18:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_remove_pedido_adicional'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='sector',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_bebida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_bebida', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_cafe_te',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_cafe_te', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_guarnicion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_guarnicion', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_plato_principal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_plato', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_postre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_postre', to='App.adicional'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero_mesa',
            field=models.IntegerField(unique=True),
        ),
        migrations.CreateModel(
            name='Pedido_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(default=django.utils.timezone.now)),
                ('adicional_bebida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_bebida_cliente', to='App.adicional')),
                ('adicional_cafe_te', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_cafe_te_cliente', to='App.adicional')),
                ('adicional_guarnicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_guarnicion_cliente', to='App.adicional')),
                ('adicional_plato_principal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_plato_cliente', to='App.adicional')),
                ('adicional_postre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_postre_cliente', to='App.adicional')),
                ('bebida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.bebida')),
                ('cafe_te', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.cafete')),
                ('guarnicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.guarnicion')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.mesa')),
                ('plato_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.comida')),
                ('postre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.postre')),
            ],
        ),
    ]
