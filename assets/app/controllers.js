(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('IndexController', IndexController)
    .controller('SignupController', SignupController)
  ;

  function SignupController ($scope, $state, $stateParams, UserService) {
    var self = this;

    self.signUp = signUp;

    // signup form
    function signUp (form) {
      form['key'] = $stateParams.invitationKey;

      UserService.signup(form).then(function(resp) {
        $state.go('index');
      }).catch(function(error) {
        self.error_msg = error.data.non_field_errors;
      });
    };
  }

  function IndexController ($scope, $state, UserService) {
    var self = this;

    self.currentView = 'login';
    
    self.login = login;
    self.actionView = actionView;

    // login form
    function login (form) {
      UserService.login(form).then(function(resp) {
        window.location.reload();
      }).catch(function(error){
        self.error_msg = error.data;
      });
    };

    // change view action
    function actionView (action) {
      self.currentView = action;
    };

  };

})();