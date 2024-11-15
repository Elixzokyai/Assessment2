from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class Contact(models.Model):
    name = models.CharField(max_length=50)  # Maximum length of 50 characters
    email = models.EmailField()
    phone = models.CharField(
        max_length=25,  # Maximum length for phone numbers
        validators=[RegexValidator(r'^\+?\d{10,15}$', message="Enter a valid phone number.")]
    )  # Allows numeric characters and an optional '+' for international numbers
    message = models.TextField(
        validators=[MinLengthValidator(100)]  # Enforce a minimum length of 100 characters
    )

    def __str__(self):
        return f'{self.name} | {self.email} | {self.phone} | {self.message[:100]}...'  # Truncated message


