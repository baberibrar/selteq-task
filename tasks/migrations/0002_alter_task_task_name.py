# Generated by Django 4.2.9 on 2024-01-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
