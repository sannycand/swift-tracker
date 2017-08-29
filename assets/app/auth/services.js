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
      logLoading    : false,
      currentLog    : undefined,
      projects      : [],
      active_project : [],
      archived_project : [],
      logout        : logout,
      startLog      : startLog,
      stopLog       : stopLog,
      userInvite    : userInvite,
      projectMember : projectMember,
      users         : users,
      addProjectMember: addProjectMember,
      addProject : addProject,
      updateProject : updateProject
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
      if (service.logLoading) return;
      service.logLoading = true;
      return $http.get('api/projects/current/log/').then(function(resp){
        service.logLoading = false;
        service.currentLog = resp.data;
      });
    };

    function getProjects() {
      if (service.loading) return;
      service.loading = true;
      return $http.get('api/projects/').then(function(resp){
        service.loading = false;
        service.projects = resp.data;
      });
    };

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

    function updateProject(project_id, form) {
      return $http.put('api/projects/' + project_id + '/', form);
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