# Generated by Django 5.1.3 on 2024-11-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_task_complexity_remove_task_urgency'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='reminder_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
