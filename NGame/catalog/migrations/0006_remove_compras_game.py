# Generated by Django 5.0.6 on 2024-07-26 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_compras'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='game',
        ),
    ]
