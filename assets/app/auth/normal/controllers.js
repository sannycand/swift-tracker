(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('DashboardController', DashboardController)
    .controller('AsideController', AsideController)
  ;

  function DashboardController ($scope) {
    var self = this;
  
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
        console.log(self.user, 'current')
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