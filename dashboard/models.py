from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User
    name = models.CharField(max_length=255, blank=True, null=True)  # Add a name field
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Add profile picture

    def __str__(self):
        return f'{self.user.username} Profile'

class IndicatorModel(models.Model):
    """
    Model for storing indicator data.
    """
    name = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.name}: {self.value}"
    
class ChartModel(models.Model):
    """
    Model for storing chart name data.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DataPointModel(models.Model):
    """
    Model for storing chart data points.
    """
    chart = models.ForeignKey(ChartModel, on_delete=models.CASCADE, related_name="data_points")
    label = models.CharField(max_length=100)  # X-axis
    value = models.IntegerField()             # Y-axis

    def __str__(self):
        return f"{self.label}: {self.value}"
