# Generated by Django 5.1.3 on 2024-11-14 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_task_completed_remove_task_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complexity',
        ),
        migrations.RemoveField(
            model_name='task',
            name='urgency',
        ),
    ]