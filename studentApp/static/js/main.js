var studentApp = angular.module("StudentApp", ["ngRoute"]);

// Controllers
studentApp.controller("StudentController", ["$scope", "$http", "$location", function($scope, $http, $location){
	$scope.students = [];
	$http.get("/api/v1/student?format=json").success(function(data){
		console.log(data);
		$scope.students = data.objects;
	});

	$scope.addstudent = function(){
		data = {
			"student_id": $scope.add.student_id,
			"name": $scope.add.student_name,
			"age": $scope.add.student_age,
			"student_class": $scope.add.student_class
		}
		$http.post("/api/v1/student/?format=json",data).success(function(data){
			$location.path('/students')
		});
	}
}]);

studentApp.controller("BehaviourController", ["$scope", "$http", "$location", function($scope, $http, $location){
	$scope.behaviours = [];
	$http.get("/api/v1/behaviour?format=json").success(function(data){
		console.log(data);
		$scope.behaviours = data.objects;
	});

	$scope.addbehaviour = function(){
		data = {
			"behaviour_id": $scope.add.behaviour_id,
			"name": $scope.add.behaviour_name,
			"points": $scope.add.behaviour_points,
		}
		$http.post("/api/v1/behaviour/?format=json",data)
			.success(function(data){
				$location.path('/behaviours')
			});
	}

}]);

studentApp.controller("AttendanceListController", ["$scope", "$http", function($scope, $http){
	$scope.attendance = [];
	$http.get("/api/v1/attendance?format=json").success(function(data){
		console.log(data);
		$scope.attendance = data.objects;
	});
}]);


studentApp.controller("PointController", ["$scope", "$http", "$location", function($scope, $http, $location){
	$scope.students = [];
	$scope.add = {
		student: {},
		behaviour: {}
	}

	$http.get("/api/v1/student?format=json").success(function(data){
		$scope.students = data.objects;
		$scope.add.student = $scope.students[0];
	});

	$scope.behaviours = [];
	$http.get("/api/v1/behaviour?format=json").success(function(data){
		$scope.behaviours = data.objects;
		$scope.add.behaviour = $scope.behaviours[0];
	});

	$scope.points = [];
	$http.get("/api/v1/point?format=json").success(function(data){
		$scope.points = data.objects;
	});

	window.add = $scope.addpoint = function(){
		delete $scope.add.student.points
		delete $scope.add.student.cname
		delete $scope.add.student.lastDate

		data = {
			"student": $scope.add.student,
			"behaviour":$scope.add.behaviour
		}
		$http.post("/api/v1/point/?format=json",data).success(function(data){
			$location.path('/points')
		});
	}
}]);



// Routes
studentApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/students', {
				templateUrl: '/static/templates/students/index.html',
				controller: 'StudentController'
			}).
			when('/behaviours', {
				templateUrl: '/static/templates/behaviour/index.html',
				controller: 'BehaviourController'
			}).	
			when('/attendance', {
				templateUrl: '/static/templates/attendance/index.html',
				controller: 'AttendanceListController'
			}).	
			when('/points', {
				templateUrl: '/static/templates/point/index.html',
				controller: 'PointController'
			}).
			when('/',{
				templateUrl:'/static/templates/students/index.html',
				controller: 'StudentController'
			}).
			when('/students/new',{
				templateUrl:'/static/templates/students/new.html',
				controller: 'StudentController'
			}).
			when('/behaviours/new', {
				templateUrl: '/static/templates/behaviour/new.html',
				controller: 'BehaviourController'
			}).
			when('/points/new', {
				templateUrl: '/static/templates/point/new.html',
				controller: 'PointController'
			}).
			otherwise({
				redirectTo: "/"
			})
}]);