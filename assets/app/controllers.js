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

  function AsideController ($scope, $state, UserService) {
    var self = this;

    self.currentView = 'login';
    
    self.signUp = signUp;
    self.login = login;
    self.actionView = actionView;


    // signup form
    function signUp (form) {
      UserService.signup(form).then(function(resp) {
        self.error_msg = '';
        self.form = {}; // reset form
      }).catch(function(error) {
        self.error_msg = error.data;
      });
    };

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