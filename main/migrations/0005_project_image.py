# Generated by Django 2.2.5 on 2020-03-30 11:57

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200330_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.upload_image_path),
        ),
    ]