var footballApp = angular.module('footballApp', [])

footballApp.controller('FootballControler', function ($scope, $http) {
    $scope.events = {}
    
    $scope.initFunc = function(){
        
        $http.get('/football/api_events_prematch/').then(function (response) {
            $scope.events = response.data;
        })
    }

    $scope.initFunc()
})