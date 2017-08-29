(function () {
  'use strict';

  angular.module('tracker', [
    'ui.router',
    'ui.bootstrap',
    'xeditable',
    'timer',
    'moment-picker',
    'multipleSelect',
    'angular.filter'
    ])
    .constant('TEMPLATE_URL', '/static/app/templates/')
    .config(csrf)
    .run(function(editableOptions) {
      editableOptions.theme = 'bs3';
    });
  ;

  // CSRF TOKEN 
  function csrf($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  };

})();