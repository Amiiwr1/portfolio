# Generated by Django 2.2.5 on 2020-03-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('mid-level', 'Mid-Level'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=120),
        ),
    ]
