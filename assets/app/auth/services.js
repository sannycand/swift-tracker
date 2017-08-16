(function () {
  'use strict';

  angular
    .module('tracker')
    .service('AuthService', AuthService)
  ;

  function AuthService ($http, Upload) {

    var service = {
      logout : logout
    };

    return service;

    function logout() {
      return $http.get('/api/logout/');
    };

  
  };

})();