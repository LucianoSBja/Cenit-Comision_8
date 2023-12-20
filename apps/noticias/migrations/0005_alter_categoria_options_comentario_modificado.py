# Generated by Django 4.2.3 on 2023-12-17 22:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_alter_noticia_options_rename_fecha_noticia_creado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('nombre',)},
        ),
        migrations.AddField(
            model_name='comentario',
            name='modificado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]