from django.db import models
from datetime import datetime, timedelta
from pytz import timezone
import pytz

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key = True)
    name = models.TextField()
    age = models.IntegerField()
    student_class = models.IntegerField()
    

class Attendance(models.Model):
	student = models.ForeignKey(Student)
	date = models.DateField(auto_now_add = True)
	time = models.DateTimeField(auto_now_add = True)
	 

class Behaviour(models.Model):
	behaviour_id =  models.IntegerField(primary_key = True)
	name = models.TextField()
	points = models.IntegerField()

# class PointManager(models.Manager):
# 	def add_point(self, student, behaviour):
# 		attendance = Attendance(student = student)
# 		point  = Point(student = student, behaviour = behaviour)
# 		point.save()
# 		attendance.save()
# 		return point

class Point(models.Model):
	student = models.ForeignKey(Student)
	behaviour = models.ForeignKey(Behaviour)
	def save(self,*args,**kwargs):
		if self.pk is None:
			attendance = Attendance(student = self.student)
			attendance.save()
		super(Point,self).save(*args,**kwargs)



    
'''
Table 1: User Account ( student_id, Name, Age, Class) 
Table 2: Attendance ( id, student_id, Date, Time)
Table 3: Points: ( id, student_id, points) ( you can assume 3 sets of points for each behavior)
Table 4: Behavior  ( id, Behaviour Name, Points )  { [1, Doing homework, 3],[2, Disrupting class, -2], [ 3, helping, 5] }
'''