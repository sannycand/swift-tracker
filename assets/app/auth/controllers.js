(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('DashboardController', DashboardController)
    .controller('AuhtAsideController', AuhtAsideController)
  ;

  function DashboardController ($scope) {
    var self = this;
  
  };

  function AuhtAsideController ($scope) {
    console.log('auth AuhtAsideController')
  }


})();