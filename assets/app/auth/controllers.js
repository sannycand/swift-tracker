(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('DashboardController', DashboardController)
    .controller('AuthAsideController', AuthAsideController)
  ;

  function DashboardController ($scope) {
    var self = this;
  
  };

  function AuthAsideController ($scope) {
    console.log('auth AuhtAsideController')
  }


})();