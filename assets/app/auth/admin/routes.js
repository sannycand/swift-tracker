(function () {
  'use strict';

  angular
    .module('tracker')
    .config(routes)

  function routes ($urlMatcherFactoryProvider, $stateProvider,
    $locationProvider, $urlRouterProvider, TEMPLATE_URL) {

    $urlRouterProvider.otherwise('/');
    $urlMatcherFactoryProvider.strictMode(false);
    $locationProvider.html5Mode(true);

    $stateProvider
      .state('legacy', {
        abstract : true,
        url      : '',
        template : '<ui-view></ui-view>'
      })
      .state('projects', {
        url          : '/',
        templateUrl  : TEMPLATE_URL + 'admin/project.html',
        controller   : 'ProjectController',
        controllerAs : 'ctrl'
      })
    ;

  };

})();