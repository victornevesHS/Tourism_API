# Generated by Django 4.2.1 on 2023-05-11 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_pontoturistico_endereco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='avaliacao',
            new_name='avaliacoes',
        ),
    ]
