# Generated by Django 3.2.9 on 2022-01-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_messages_roomname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='roomName',
            field=models.CharField(max_length=10000000),
        ),
    ]