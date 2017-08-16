(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('IndexController', IndexController)
    .controller('AsideController', AsideController)
  ;

  function IndexController ($scope) {
    var self = this;
  
  };

  function AsideController ($scope, UserService) {
    var self = this;

    self.signUp = signUp;

    // signup form
    function signUp (form) {
      UserService.signup(form).then(function(resp) {
        self.error_msg = '';
        self.form = {}; // reset form
      }).catch(function(error) {
        self.error_msg = error.data;
      });
    };

  };

})();