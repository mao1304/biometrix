# Generated by Django 4.2.6 on 2023-11-04 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_alter_clase_profesor_id'),
        ('usuario', '0009_newuser_remove_normaluser_groups_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NormalUser',
        ),
    ]
