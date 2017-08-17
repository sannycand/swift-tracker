(function () {
  'use strict';

  angular.module('tracker', [
    'ui.router',
    'ui.bootstrap'
    ])
    .constant('TEMPLATE_URL', '/static/app/templates/')
    .config(csrf)
  ;

  // CSRF TOKEN 
  function csrf($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  };

})();