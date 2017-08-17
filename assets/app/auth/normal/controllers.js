(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('DashboardController', DashboardController)
    .controller('AsideController', AsideController)
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

})();