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
      .state('login', {
        url          : '/',
        templateUrl  : TEMPLATE_URL + 'login.html',
        controller   : 'LoginController',
        controllerAs : 'ctrl'
      })
      .state('signup', {
        url          : '/signup-:invitationKey/',
        templateUrl  : TEMPLATE_URL + 'signup.html',
        controller   : 'SignupController',
        controllerAs : 'ctrl'
      })


    ;

  };

})();