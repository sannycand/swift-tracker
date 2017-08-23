(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('ProjectController', ProjectController)
    .controller('AsideController', AsideController)
  ;

  function ProjectController ($scope, AuthService) {
    var self = this;

    self.AuthService = AuthService;
  };

  function AsideController ($scope, $uibModal, AuthService) {
    var self = this;

    self.logout = logout;
    self.toggle = toggle;
    self.inviteBtn = inviteBtn;

    // get current user data
    $scope.$watch(function(){
      return AuthService.loaded;
    },function(isReady) {
      if(!isReady) {
        self.user = AuthService.user;
      };
    });

    // user logout
    function logout () {
      AuthService.logout().then(function(resp){
        window.location.reload();
      });
    };

    function inviteBtn () {
      var modalInstance = $uibModal.open({
        animation: true,
        ariaLabelledBy: 'modal-title',
        ariaDescribedBy: 'modal-body',
        templateUrl: 'invite.html',
        size: 'md',
        controllerAs: 'ctrl',
        controller: function($uibModalInstance, AuthService) {
          self = this;

          self.save = function (data) {
            self.loading = true;
            AuthService.userInvite(data).then(function(resp){
              self.loading = false;
              $uibModalInstance.close();
            }).catch(function(error) {
              self.loading = false;
              self.error_msg = error.data.email[0];  
            });
          };

          self.cancel = function () {
            $uibModalInstance.dismiss('cancel');
          };
        }

      });
    };

    // toggle nav
    function toggle () {
      angular.element(document.getElementById("nav-collapse")).toggleClass("is-open");
    };
  };
})();