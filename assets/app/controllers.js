(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('LoginController', LoginController)
    .controller('SignupController', SignupController)
  ;

  function SignupController ($scope, $state, $stateParams, UserService) {
    var self = this;

    self.currentView = 'no-sidebar';
    
    self.signUp = signUp;

    // signup form
    function signUp (form) {
      form['key'] = $stateParams.invitationKey;

      UserService.signup(form).then(function(resp) {
        $state.go('login');
      }).catch(function(error) {
        self.error_msg = error.data;
      });
    };
  }

  function LoginController ($scope, $state, UserService) {
    var self = this;

    self.currentView = 'no-sidebar';
    
    self.login = login;
    self.change = change

    // remove backend error
    function change () {
      self.error_msg = undefined;
    };

    // login form
    function login (form) {
      UserService.login(form).then(function(resp) {
        window.location.reload();
      }).catch(function(error){
        self.error_msg = error.data.non_field_errors[0];
      });
    };

  };

})();