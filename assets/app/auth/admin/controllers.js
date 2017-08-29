(function () {
  'use strict';

  angular
    .module('tracker')
    .controller('ProjectController', ProjectController)
    .controller('AsideController', AsideController)
  ;

  function ProjectController ($scope, $uibModal, AuthService) {
    var self = this;
    
    self.AuthService = AuthService;
    self.toggle = toggle;
    self.addMember = addMember;
    self.addProject = addProject;
    self.updateProject = updateProject;
    self.isArchived = isArchived;
    self.isActive = isActive;

    $scope.is_archived = false;

    // show archived projects
    function isArchived () {
      $scope.is_archived = true;
    }

    // show active projects
    function isActive () {
      $scope.is_archived = false;
    }

    $scope.$watch(function(){
      return AuthService.loading;
    },function(isReady) {
      if(!isReady) {
        AuthService.archived_project = _.where(AuthService.projects, { is_archived: true });
        AuthService.active_project = _.where(AuthService.projects, { is_archived: false });
      };
    });
    
    // project toggle 
    function toggle (project) {
      if (project.is_open) {
        project.is_open = false;
      } else {
        project['is_open'] = true;
      }
    };

    function addMember (project) {
      var modalInstance = $uibModal.open({
        animation: true,
        ariaLabelledBy: 'modal-title',
        ariaDescribedBy: 'modal-body',
        templateUrl: 'addMember.html',
        size: 'md',
        controllerAs: 'ctrl',
        controller: function($uibModalInstance, $rootScope, AuthService) {
          self = this;

          self.cancel = cancel;
          self.save = save;

          // get project none members
          AuthService.users(project.id).then(function(resp){
            self.users = resp.data;
          });

          // find project index
          var index =  _.findIndex(AuthService.projects, project)

          function save (users) {
            _.each(users, function(user, i){
              
              var form = {
                "worker": user.id,
                "project": project.id
              }

              AuthService.addProjectMember(form).then(function(resp){
                AuthService.projects[index].members.push(resp.data.worker_data)
                $uibModalInstance.close();
              }).catch(function(error) {
                self.error_msg = error.data
              });
            });
          };

          function cancel () {
            $uibModalInstance.dismiss('cancel');
          };
        }

      });
    };

    function addProject (project) {
      var modalInstance = $uibModal.open({
        animation: true,
        ariaLabelledBy: 'modal-title',
        ariaDescribedBy: 'modal-body',
        templateUrl: 'addProject.html',
        size: 'md',
        controllerAs: 'ctrl',
        controller: function($uibModalInstance, AuthService) {
          self = this;

          self.change = change;
          self.save = save;
          self.cancel = cancel;

          // remove backend error
          function change () {
            self.error_msg = undefined;
          };

          function save (form) {
            AuthService.addProject(form).then(function(resp){
              AuthService.projects.push(resp.data);
              $uibModalInstance.close();
            }).catch(function(error) {
              self.error_msg = error.data
            });
          };

          function cancel () {
            $uibModalInstance.dismiss('cancel');
          };
        }

      });
    };

    function updateProject (project) {
      var modalInstance = $uibModal.open({
        animation: true,
        ariaLabelledBy: 'modal-title',
        ariaDescribedBy: 'modal-body',
        templateUrl: 'updateProject.html',
        size: 'md',
        controllerAs: 'ctrl',
        controller: function($scope, $uibModalInstance, AuthService) {
          self = this;

          self.change = change;
          self.save = save;
          self.cancel = cancel;
          self.archivedProject = archivedProject;
          self.restoreProject = restoreProject;

          self.project = project;

          // remove backend error
          function change () {
            self.error_msg = undefined;
          };

          function save (form) {
            AuthService.updateProject(project.id, form).then(function(resp){ 
              $uibModalInstance.close();
              AuthService.archived_project = _.where(AuthService.projects, { is_archived: true });
              AuthService.active_project = _.where(AuthService.projects, { is_archived: false });
            }).catch(function(error) {
              self.error_msg = error.data; 
            });
          };

          function cancel () {
            $uibModalInstance.close();
          };

          function restoreProject () {
            var index =  _.findIndex(AuthService.projects, project)
            AuthService.projects[index].is_archived = false;
          };

          function archivedProject (project) {
            var modalInstance = $uibModal.open({
              animation: true,
              ariaLabelledBy: 'modal-title',
              ariaDescribedBy: 'modal-body',
              templateUrl: 'archivedProject.html',
              size: 'md',
              controllerAs: 'ctrl',
              controller: function($scope, $uibModalInstance, AuthService) {
                var self = this;
                
                self.project = project;
                self.archived = archived;
                self.cancel = cancel;

                function archived () {
                  var index =  _.findIndex(AuthService.projects, project)

                  AuthService.projects[index].is_archived = true;
                  $uibModalInstance.close();
                };

                function cancel () {
                  $uibModalInstance.close();
                };

              }
            });
          }
        }
      });
    };
  };

  function AsideController ($scope, $uibModal, AuthService) {
    var self = this;

    self.logout = logout;
    self.toggle = toggle;
    self.inviteUser = inviteUser;

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

    function inviteUser () {
      var modalInstance = $uibModal.open({
        animation: true,
        ariaLabelledBy: 'modal-title',
        ariaDescribedBy: 'modal-body',
        templateUrl: 'invite.html',
        size: 'md',
        controllerAs: 'ctrl',
        controller: function($uibModalInstance, AuthService) {
          self = this;

          self.save = save;
          self.cancel = cancel;
          self.change = change;

          // remove backend error
          function change () {
            if (self.error_msg) {
               angular.element(document.getElementById("email")).removeClass("input-error");
              self.error_msg = undefined;
            }
          };

          function save (data) {
            self.loading = true;
            AuthService.userInvite(data).then(function(resp){
              self.loading = false;
              $uibModalInstance.close();
            }).catch(function(error) {
              self.loading = false;
              self.error_msg = error.data.email[0];  
            });
          };

          function cancel () {
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