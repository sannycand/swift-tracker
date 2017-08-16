(function () {
  'use strict';

  angular
    .module('tracker')
    .service('UserService', UserService)
  ;

  function UserService ($http) {

    var service = {
      signup : signup,
      login  : login
    };

    return service;

    function signup(form) {
      return $http.post('/api/signup/', form);
    };

    function login(form) {
      return $http.post('/api/login/', form);
    };

  };

})();