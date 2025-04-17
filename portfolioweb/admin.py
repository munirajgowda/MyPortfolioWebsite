from django.contrib import admin
from . models import BasicInfo, Projects, Achievements, achiveCategory, proCategory
from . models import Education, SkillCategory, Skills 

class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'resume_link')
    
class EducationAdmin(admin.ModelAdmin):
    list_display = ('course', 'institute', 'year_of_graduated')
    
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'category')
    
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('category')
 
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'project_link', 'completed_date')

class proCategoryAdmin(admin.ModelAdmin):
    list_display = ('proCat_name')
    
    
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'credit_link', 'completed_date')

class achiveCategoryAdmin(admin.ModelAdmin):
    list_display = ('achiveCat_name')
    


 
admin.site.register(BasicInfo,BasicInfoAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(achiveCategory)
admin.site.register(Achievements, AchievementsAdmin)
admin.site.register(proCategory)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(SkillCategory)
