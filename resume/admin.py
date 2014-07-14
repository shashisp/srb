from resume.models import personal_info, Education, Skill, Achievement
from django.contrib import admin

class pesonal_infoAdmin(admin.ModelAdmin):
	pass
class educationAdmin(admin.ModelAdmin):
	pass
class skillAdmin(admin.ModelAdmin):
	pass
class achievementAdmin(admin.ModelAdmin):
	pass

admin.site.register(personal_info, pesonal_infoAdmin)
admin.site.register(Education, educationAdmin)
admin.site.register(Skill, skillAdmin)
admin.site.register(Achievement, achievementAdmin)
