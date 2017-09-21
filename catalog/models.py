from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Category(models.Model):
    """
    Model representing a service category (e.g. Photography, Cooking).
    """
    name = models.CharField(max_length=200, help_text="Enter a category (e.g. Photography, Cooking, etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Service(models.Model):
    """
    Model representing a service.
    """
    title = models.CharField(max_length = 200)
    provider = models.CharField(max_length = 200,
                                default = "",
                                help_text = "Enter name(s) of the service provider")
    '''
    about_provider = models.TextField(max_length=1000,
                                   default = "",
                                   help_text="Enter a brief introduction of service provider")
    '''
    cost = models.CharField(max_length = 200,
                            default = "",
                            help_text = "Enter service's cost:")
    summary = models.TextField(max_length=1000,
                               default = "",
                               help_text="Enter a brief description of the service")
    availability = models.TextField(max_length=1000,
                                    default = "",
                                    help_text="Enter your availability")
    category = models.ManyToManyField(Category,
                                      default = None,
                                      help_text="Select a category for this service")
    contact = models.EmailField(max_length=254,
                                default = "null@gmail.com",
                                help_text="Enter provider's email")
    thumb_photo = models.ImageField(default = "holder.js/10s0px280/thumb", help_text = "Upload thumbnail image")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


    def get_absolute_url(self):
        """
        Returns the url to access a particular service instance.
        """
        return reverse('service-detail', args=[str(self.id)])

class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, default = 1)
    introduction = models.CharField(max_length = 1000, help_text="Tell us about yourself!")
    services_offered = models.ManyToManyField(Service, help_text="Select your service(s):")
    has_services = models.BooleanField(default = False, help_text = "Does this user have listed services?")
    contact = models.EmailField(max_length=254, default = "null@gmail.com", help_text="Enter your email")

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.user.username

    def get_absolute_url(self):
        """
        Returns the url to access a particular service instance.
        """
        return reverse('userprofiles-detail', args=[str(self.id)])
