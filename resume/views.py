from rest_framework import viewsets
from resume.models import personal_info, Skill, Education, Achievement
from resume.serializers import personal_infoSerializer, SkillSerializer, EducationSerializer, AchievementSerializer


class personal_infoViewSet(viewsets.ModelViewSet):
	queryset = personal_info.objects.all()
	serializer_class = personal_infoSerializer