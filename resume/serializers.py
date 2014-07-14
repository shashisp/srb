from resume.models import personal_info, Education, Skill, Achievement
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skill
		fields = ('skill_name')

class EducationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = ('college_name', 'from_date', 'to_date')


class AchievementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Achievement
		fields = ('award_name', 'date')

class personal_infoSerializer(serializers.ModelSerializer):
	#skill = SkillSerializer(many=True)
	education = EducationSerializer(many=True)
	achievement = AchievementSerializer(many=True)


	class Meta:
		model = personal_info
		fields = ('address', 'city', 'objective', 'email', 'contact_no', 'profile_name', 'pincode','skill', 'education', 'achievement')


'''

class CreateResumeSerializer(serializers.ModelSerializer):

	class Meta:
		model = personal_info
		fields = ('address', 'city', 'objective', 'email', 'contact_no', 'profile_name', 'pincode' )

		def restore_object(self, attrs, instance=None):

			assert instance is None:
			personal_info = personal_info(pid=attrs['pid'] ,address=attrs['address'], city=attrs['city'], objective=attrs['objective'], email=attrs['email'], contact_no=attrs['contact_no'], profile_name=attrs['profile_name'], pincode=attrs['pincode'], skill=attrs['skill'], education=attrs['education'], achievement=attrs['achievement'])
'''