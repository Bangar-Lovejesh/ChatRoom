# Generated by Django 3.2.9 on 2022-01-03 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Messages',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]