# Generated by Django 5.0.4 on 2024-05-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, upload_to='todo'),
        ),
    ]