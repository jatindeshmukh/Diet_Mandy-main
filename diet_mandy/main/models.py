from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=15, null=True, blank=True)
#     address = models.TextField(null=True, blank=True)
#     city = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    full_name = models.CharField(null=True, blank=True)
    contact_number = models.CharField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(null=True, blank=True)

    height = models.CharField(null=True, blank=True)  # 170 cm or 5'6"

    goal_choices = (
        ('Weight Loss', 'Weight Loss'),
        ('Weight Gain', 'Weight Gain'),
        ('Muscle Gain', 'Muscle Gain'),
        ('Healthy Lifestyle', 'Healthy Lifestyle'),
    )
    primary_goal = models.CharField(null=True, blank=True)

    diet_choices = (
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
        ('Vegan', 'Vegan'),
        ('Keto', 'Keto'),
        ('Other', 'Other'),
    )
    diet_type = models.CharField(null=True, blank=True)

    allergies = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username