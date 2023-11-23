# Generated by Django 4.2.5 on 2023-09-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_alter_client_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='client',
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='Anonymous', max_length=64),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]