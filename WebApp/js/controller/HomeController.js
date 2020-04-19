var homeController = function($scope, $mdToast, empresaApi) {

  $scope.empresas = [];

  $scope.listar = function() {
    empresaApi.listar()
      .then(function(response) {
        $scope.empresas = response.data;
      })
      .catch(function(error) {
        var toast = $mdToast.simple()
          .textContent("Problema para exibir a lista de empresas.")
          .position('top right')
          .action('OK')
          .hideDelay(6000);
        $mdToast.show(toast);
      });
  };

  $scope.pesquisar = function(nome) {
    if (nome.length >= 3) {
      empresaApi.buscarPorNome(nome)
        .then(function(response) {
          $scope.empresas = response.data;
        })
        .catch(function(error) {

        });
    }
  };

  $scope.enviarContato = function() {
    console.log("enviando contato.");
  }

  $scope.listar();

  // Paginação da tabela.
  $scope.query = {
        order: 'municipio',
        limit: 8,
        page: 1
    };
}

app.controller('HomeController', homeController);
