# Generated by Django 2.0.6 on 2020-06-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flores', '0002_auto_20200613_0123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flores',
            new_name='Flor',
        ),
        migrations.AlterModelOptions(
            name='flor',
            options={'verbose_name': 'Flor', 'verbose_name_plural': 'Flores'},
        ),
    ]