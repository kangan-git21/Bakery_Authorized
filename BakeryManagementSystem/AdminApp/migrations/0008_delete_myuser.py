# Generated by Django 4.1 on 2022-08-17 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0007_myuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]