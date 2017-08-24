(function () {
  'use strict';

  angular
    .module('tracker')
    .service('AuthService', AuthService)
  ;

  function AuthService ($http) {


    var service = {
      user          : undefined,
      loaded        : false,
      loading       : false,
      projects      : [],
      currentLog    : undefined,
      logout        : logout,
      startLog      : startLog,
      stopLog       : stopLog,
      userInvite    : userInvite,
      projectMember : projectMember,
      users         : users,
      addProjectMember: addProjectMember,
      addProject : addProject
    };

    getCurrentUser();
    getProjects();
    getCurrentLog();

    return service;

    function getCurrentUser() {
      if (service.loaded) return;
      service.loaded = true;
      return $http.get('api/auth/user/').then(function(resp){
        service.loaded = false;
        service.user = resp.data;
      });
    };

    function getCurrentLog() {
      if (service.loading) return;
      service.loading = true;
      return $http.get('api/projects/current/log/').then(function(resp){
        service.loading = false;
        service.currentLog = resp.data;
      });
    };

    function getProjects() {
      return $http.get('api/projects/').then(function(resp){
        service.projects = resp.data;
      });
    }

    function logout() {
      return $http.get('/api/logout/');
    };

    function users(project_id) {
      return $http.get('api/projects/'+ project_id +'/users/');
    }

    function addProjectMember(form) {
      return $http.post('api/projects/add/member/', form);
    }

    function addProject(form) {
      return $http.post('api/projects/add/', form);
    }

    function projectMember() {
      return $http.get('api/projects/member/');
    };

    function startLog(project_id, form) {
      return $http.post('api/projects/'+ project_id +'/log/', form);
    };

    function stopLog(form) {
      return $http.put('api/projects/stop/log/', form);
    }

    function userInvite(form) {
      return $http.post('api/user/invite/', form);
    }
  
  };

})();