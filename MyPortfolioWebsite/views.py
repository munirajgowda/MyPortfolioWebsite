from django.shortcuts import render
from portfolioweb.models import BasicInfo, Projects, proCategory, ExternalLink
from portfolioweb.models import Achievements, achiveCategory
from portfolioweb.models import Education, SkillCategory, Skills 
from urllib.parse import unquote
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import tldextract
from urllib.parse import urlparse



def home(request):
    basic_info = BasicInfo.objects.first()  
    selected_category = unquote(request.GET.get('category', 'All'))
    external_links = ExternalLink.objects.filter(basic_info=basic_info)



    if selected_category == "All" or not selected_category:
        projects = Projects.objects.order_by('-completed_date')[:6]  # Show recent 6 projects
    else:
        projects = Projects.objects.filter(category__proCat_name=selected_category).order_by('-completed_date')[:6]

    categories = proCategory.objects.filter(projects__isnull=False).distinct()

    context = {
        'basic_info': basic_info,
        'projects': projects,
        'categories': categories,
        'selected_category': selected_category,
        'external_links': external_links,
    }
    return render(request, 'Home.html', context)



# Education View
def education(request):
    educations = Education.objects.order_by('-year_of_graduated')
    skill_categories = SkillCategory.objects.prefetch_related('skills_set').all()
    basic_info = BasicInfo.objects.first()
    external_links = ExternalLink.objects.filter(basic_info=basic_info)
    
    context = {
        'educations': educations,
        'skill_categories': skill_categories,
        'external_links': external_links,
    }
    return render(request, 'Education.html', context)


# Projects View
def projects(request): 
    projects = Projects.objects.order_by('-completed_date')  # Get all projects, most recent first
    categories = proCategory.objects.filter(projects__isnull=False).distinct()  # Get only used categories
    selected_category = unquote(request.GET.get('category', 'All'))
    basic_info = BasicInfo.objects.first()
    external_links = ExternalLink.objects.filter(basic_info=basic_info)
    
    if selected_category == "All" or not selected_category:
        projects = Projects.objects.order_by('-completed_date')
    else:
        projects = Projects.objects.filter(category__proCat_name=selected_category).order_by('-completed_date')

    categories = proCategory.objects.filter(projects__isnull=False).distinct()

    context = {
        'projects': projects,
        'categories': categories,  # Passing categories for filtering
        'selected_category': selected_category,
        'external_links': external_links,
    }
    return render(request, 'Projects.html', context)


def get_domain_info(url):
    parsed_url = urlparse(url)
    extracted = tldextract.extract(parsed_url.netloc)
    domain = f"{extracted.domain}.{extracted.suffix}"
    favicon_url = f"https://www.google.com/s2/favicons?domain={parsed_url.netloc}&sz=64"
    return domain, favicon_url

def single_project(request, slug):
    project = get_object_or_404(Projects, slug=slug)
    basic_info = BasicInfo.objects.first()
    external_links = ExternalLink.objects.filter(basic_info=basic_info)

    project_domain, project_favicon = (None, None)
    if project.project_link:
        project_domain, project_favicon = get_domain_info(project.project_link)

    context = {
        'project': project,
        'external_links': external_links,
        'project_domain': project_domain,
        'project_favicon': project_favicon,
    }
    return render(request, 'singleProject.html', context)


# Achievements View
def achievements(request):
    selected_category = unquote(request.GET.get('category', 'All'))
    basic_info = BasicInfo.objects.first()
    external_links = ExternalLink.objects.filter(basic_info=basic_info)

    if selected_category == "All" or not selected_category:
        achievements = Achievements.objects.order_by('-completed_date')
    else:
        achievements = Achievements.objects.filter(category__achiveCat_name=selected_category).order_by('-completed_date')

    categories = achiveCategory.objects.filter(achievements__isnull=False).distinct()

    context = {
        'achievements': achievements,
        'categories': categories,
        'selected_category': selected_category,
        'external_links': external_links,
    }
    return render(request, 'Achievements.html', context)