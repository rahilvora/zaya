from tastypie.resources import ModelResource
from tastypie import fields
from studentApp.models import *
from tastypie.authorization import Authorization


class StudentResource(ModelResource):
	cname = fields.CharField()
	points = fields.IntegerField()
	lastDate = fields.DateField()

	def dehydrate_cname(self, bundle):
		return bundle.obj.name.upper()

	def dehydrate_points(self, bundle):
		points = bundle.obj.point_set.all()
		return reduce(lambda total,point: total + point.behaviour.points, points, 0)
	
	def dehydrate_lastDate(self,bundle):
		try:
			return bundle.obj.attendance_set.latest("time").time.strftime("%d %b, %Y | %H:%M")
		except:
			return 'absent'

	class Meta:
		queryset = Student.objects.all()
		authorization = Authorization()

class BehaviourResource(ModelResource):
    class Meta:
        queryset = Behaviour.objects.all()
        authorization = Authorization()

class AttendanceResource(ModelResource):
	student = fields.ToOneField(StudentResource,'student', null=True, full=True)
	class Meta:
		queryset = Attendance.objects.all()
		authorization = Authorization()
		allowed_methods = ['get'] 

class PointResource(ModelResource):
	student = fields.ForeignKey(StudentResource, "student")
	behaviour = fields.ForeignKey(BehaviourResource, "behaviour")
	student = fields.ToOneField(StudentResource,'student',null=True,full=True)
	behaviour = fields.ToOneField(BehaviourResource,'behaviour',null=True,full=True)
	class Meta:
		queryset = Point.objects.all()
		authorization = Authorization()