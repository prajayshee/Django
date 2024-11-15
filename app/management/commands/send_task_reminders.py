# app/management/commands/send_task_reminders.py
import logging
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from app.models import Task

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Sends task reminders to users'

    def handle(self, *args, **kwargs):
        tasks = Task.objects.filter(reminder_time__lte=timezone.now(), reminder_time__isnull=False)
        for task in tasks:
            try:
                send_mail(
                    'Reminder: Task Due Soon',
                    f'Your task "{task.title}" is due soon.',
                    'prajaysheechauhan@gmail.com',
                    ['prajayshee.chauhan@mitpwu.edu.in'],  # Replace with actual user emails
                    fail_silently=False,
                )
                logger.info(f"Reminder email sent for task: {task.title}")
            except Exception as e:
                logger.error(f"Failed to send reminder for {task.title}: {e}")
        self.stdout.write(self.style.SUCCESS('Successfully processed task reminders'))
