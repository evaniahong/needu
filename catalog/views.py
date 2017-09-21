from django.shortcuts import render

# Create your views here.

from .models import Service, Category, UserProfile

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_services=Service.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_services':num_services},
    )

from django.views import generic

class CategoryListView(generic.ListView):
    model = Category

class ServiceListView(generic.ListView):
    model = Service

class ServiceDetailView(generic.DetailView):
    model = Service

class UserProfileListView(generic.ListView):
    model = UserProfile

class UserProfileDetailView(generic.DetailView):
    model = UserProfile
