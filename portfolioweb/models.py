from django.db import models
from urllib.parse import urlparse

class BasicInfo(models.Model):
    name = models.CharField(max_length=100, default="Muniraju B R", editable=False)  
    designation = models.CharField(max_length=100)
    about = models.TextField()
    resume_link = models.URLField(max_length=500, blank=True) 
    profile_picture = models.ImageField(upload_to='uploads/profile_picture/%y/%m/%d')

    class Meta:
        verbose_name_plural = 'Basic Info'
    
    def __str__(self):
        return self.name


class ExternalLink(models.Model):
    basic_info = models.ForeignKey(BasicInfo, on_delete=models.CASCADE, related_name='external_links')
    name = models.CharField(max_length=100)
    url = models.URLField()

    def icon_class(self):
        domain_map = {
            'github': 'fab fa-github',
            'linkedin': 'fab fa-linkedin',
            'twitter': 'fab fa-twitter',
            'instagram': 'fab fa-instagram',
            'facebook': 'fab fa-facebook',
            'youtube': 'fab fa-youtube',
            'behance': 'fab fa-behance',
            'dribbble': 'fab fa-dribbble',
            'codepen': 'fab fa-codepen',
            'stack': 'fab fa-stack-overflow',
            'replit': 'fas fa-code',
            'site': 'fas fa-globe',
        }
        for keyword, icon in domain_map.items():
            if keyword in self.url.lower() or keyword in self.name.lower():
                return icon
        return 'fas fa-link'  # Default



class proCategory(models.Model):
    proCat_name = models.CharField(max_length=50, unique=True)

    class Meta:
            verbose_name_plural = 'proCategories'

    def __str__(self):
        return self.proCat_name

STATUS_CHOICE = (
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed')
)    

class Projects(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    description = models.TextField()
    category = models.ForeignKey(proCategory, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default='ongoing')
    completed_date = models.DateField(null=True, blank=True)
    project_link = models.URLField(max_length=500, blank=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name_plural = 'Projects'


class achiveCategory(models.Model):
    achiveCat_name = models.CharField(max_length=50, unique=True) 
    class Meta:
            verbose_name_plural = 'achiveCategory'

    def __str__(self):
        return self.achiveCat_name

class Achievements(models.Model):
    title = models.CharField(max_length=100, unique=True)
    thumbnail_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    category = models.ForeignKey(achiveCategory, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default='ongoing')
    completed_date = models.DateField(null=True, blank=True)
    credit_link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name_plural = 'Achievements'
            
            
class Education(models.Model):
    course = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year_of_graduated = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.course

    class Meta:
        verbose_name_plural = 'Education'


class SkillCategory(models.Model):
    skillCat_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Skill Categories'

    def __str__(self):
        return self.skillCat_name


class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name_plural = 'Skills'
