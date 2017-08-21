(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('DashboardController', DashboardController)
    .controller('AsideController', AsideController)
    .controller('TrackerController', TrackerController)
  ;

  function DashboardController ($scope, AuthService) {
    var self = this;

    self.toggle = toggle;

    // get current user projects
    AuthService.projectMember().then(function(resp){
      self.projects = resp.data;
    });

    // project toggle 
    function toggle (id) {
      var projectID = "collapse-" + id;
      angular.element(document.getElementById(projectID)).toggleClass("is-open");
    };
  
  };

  function AsideController ($scope, AuthService) {
    var self = this;

    self.logout = logout;
    self.toggle = toggle;

    // get current user data
    $scope.$watch(function(){
      return AuthService.loaded;
    },function(isReady) {
      if(!isReady) {
        self.user = AuthService.user;
      };
    });

    // user logout
    function logout () {
      AuthService.logout().then(function(resp){
        window.location.reload();
      });
    };

    // toggle nav
    function toggle () {
      angular.element(document.getElementById("nav-collapse")).toggleClass("is-open");
    };

  };

  function TrackerController($scope, $timeout, AuthService) {
    var self = this;

    self.isReady = false;
    self.currentLog = {};
    self.startLog = startLog;
    self.stopLog = stopLog;
    self.ready = ready;

    // get current user projects
    AuthService.projectMember().then(function(resp){
      self.projects = resp.data;
    });

    // get current log
    AuthService.currentLog().then(function(resp){

      self.currentLog = resp.data;

      if (self.currentLog) {
        var project = _.find(self.projects, function(item){
            return item.project.id == self.currentLog.project.id;
        });
        
        if (project) {
          self.timerRunning = true;
          $scope.description = self.currentLog.description;
          $scope.project = project;
          console.log(self.currentLog)
        };
      };

    });

    // enabled start button
    function ready(project, desc) {
      var projectSelected = _.find(self.projects, function(item){
          return item == project;
      });

      if (projectSelected) {
        if (desc) {
          self.isReady = true;
          projectSelected['is_ready'] = true;
          $scope.project = projectSelected;
        } else {
          self.isReady = false;
          projectSelected['is_ready'] = false;
          $scope.project = projectSelected;
        };
      };
    };

    // start log
    function startLog(project_id, desc) {
      var form = {
        "description": desc
      }

      if (self.isReady) {
        AuthService.startLog(project_id, form).then(function(resp){
          self.currentLog = resp.data;
          self.timerRunning = true;
          $scope.$broadcast('timer-start');
        });
      };

    };

    // stop log
    function stopLog(data, desc) {
      data.description = desc
      AuthService.stopLog(data).then(function(resp){
        $scope.description = '';
        self.currentLog = {};
        self.timerRunning = false;
      });
    };

  };


})();