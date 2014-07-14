from django.db import models

class Skill(models.Model):
	skill_name = models.CharField(max_length=100)


	def __unicode__(self):
		return self.skill_name

	

class Education(models.Model):
	college_name = models.CharField(max_length=200)
	from_date = models.CharField(max_length=10)
	to_date = models.CharField(max_length=10)

	def __unicode__(self):
		return self.college_name

	


class Achievement(models.Model):
	award_name = models.CharField(max_length=100)
	date = models.CharField(max_length=100)

	def __unicode__(self):
		return self.award_name

	
	

class personal_info(models.Model):
	address = models.TextField()
	objective = models.TextField()
	city = models.CharField(max_length=100)
	email = models.EmailField()
	contact_no = models.CharField(max_length=100)
	profile_name = models.CharField(max_length=100)
	pincode = models.CharField(max_length=100)
	skill = models.ManyToManyField(Skill)
	education = models.ManyToManyField(Education)
	achievement = models.ManyToManyField(Achievement)


	def __unicode__(self):
		return self.profile_name
		

	






	



