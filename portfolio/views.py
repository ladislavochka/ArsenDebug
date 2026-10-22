from django.shortcuts import render

# Create your views here.
def home_views(request):
    return render(request, 'portfolio/home.html')
def projects_views(request):
    return render(request, 'portfolio/projects.html')
def skills_views(request):
    return render(request, 'portfolio/skills.html')
