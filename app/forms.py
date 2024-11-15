from datetime import date
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'reminder_time', 'priority']  # Include reminder_time

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'reminder_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Allow the user to pick a date & time
        }
        
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < date.today():
            raise forms.ValidationError("The due date cannot be in the past.")
        return due_date


# For user signup:
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Ensure both passwords match
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        # You could add more checks like password strength if needed
        
        return cleaned_data

    def save(self, commit=True):
        # Create the user, hash the password, and save it
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password before saving
        if commit:
            user.save()
        return user
