from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class GymClass(models.Model):
    name = models.CharField(max_length=255)  # Name of the class
    description = models.TextField()  # Detailed description of the class
    time = models.TimeField()  # Time of the class
    date = models.DateField()  # Date of the class
    duration = models.DurationField()  # Duration of the class
    price = models.DecimalField(max_digits=10, decimal_places=2, default=6.00 )  # Price of the class

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date', 'time']  # Orders by date first, then by time

class Booking(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('gymbro', 'GymBro')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who made the booking
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)  # Link to the GymClass
    experience_level = models.CharField(
        max_length=15, choices=EXPERIENCE_LEVEL_CHOICES, default='beginner'
    )  # Experience level as drop down box options
    further_information = models.TextField(blank=True, null=True)  # Additional information field

    def __str__(self):
        return f"Booking by {self.user.username} for {self.gym_class.name}"
    
    def final_price(self):
        """Determine the price for the booking based on membership status."""
        membership = Membership.objects.filter(user=self.user).first()
        if membership and membership.is_member:
            return 0.00  # Free for members
        return self.gym_class.price

class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to a single user
    is_member = models.BooleanField(default=False)  # Indicates if the user is a member

    def __str__(self):
        return f"{self.user.username} - {'Member' if self.is_member else 'Non-member'}"