from django.db import models

# Create your models here.

class Technologies(models.Model):
	TECH_TYPES = (
		('L','Language'),
		('Fr','Framework'),
		('T','Tools'),
		('K','Kits'),
		('E','Extension'),
		('DB','Databases')
	)
	name = models.CharField(max_length=30)
	tech_type = models.CharField(max_length=2,choices=TECH_TYPES)

class Jobs(models.Model):
	company = models.CharField(max_length=40)
	position = models.CharField(max_length=50)
	location = models.CharField(max_length=30)
	start_date = models.DateField()
	end_date = models.DateField()

class Experiences(models.Model):
        event = models.CharField(max_length=50)
        description = models.TextField()
        tech_exp = models.ManyToManyField(Technologies)
        job = models.ForeignKey(Jobs)

class Projects(models.Model):
	tech_used = models.ManyToManyField(Technologies)
	proj_description = models.TextField()
	courses = models.ForeignKey(Experiences, blank=True, null=True)

class Courses(models.Model):
	course_name = models.CharField(max_length=30)
	course_description = models.TextField()
