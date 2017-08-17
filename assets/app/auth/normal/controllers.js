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

  function AsideController ($scope) {
    console.log('auth NormalAsideController')
  }


})();