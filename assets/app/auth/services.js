(function () {
  'use strict';

  angular
    .module('tracker')
    .service('AuthService', AuthService)
  ;

  function AuthService ($http) {


    var service = {
      logout : logout,
      user   : undefined,
      loaded : false,
    };

    getCurrentUser();

    return service;

    function getCurrentUser() {
      if (service.loaded) return;
      service.loaded = true;
      return $http.get('api/auth/user/').then(function(resp){
        service.loaded = false;
        service.user = resp.data;
      });
    };

    function logout() {
      return $http.get('/api/logout/');
    };
  
  };

})();