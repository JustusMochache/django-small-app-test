# Generated by Django 3.2 on 2021-04-14 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smallapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]