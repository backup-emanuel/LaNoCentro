var empresaController = function($scope, $mdToast, $state,
  empresaApi, enderecoApi, serviceCfg) {

  $scope.empresa = {};
  $scope.endereco = {};

  $scope.cadastrar = function() {
    // Criar uma cópia da empresa e endereco do $scope.
    let endereco = angular.copy($scope.endereco);

    enderecoApi.cadastrar(endereco)
      .then(function(response) {

        let empresa = angular.copy($scope.empresa);

        // Id do endereco
        enderecoResponse = response.data;
        let endereco = {};
        endereco.id = enderecoResponse.id;
        empresa.endereco = endereco;

        // Cadastrar empresa com o endereço
        cadastrarEmpresa(empresa);
      })
      .catch(function(error) {
        // Exibir erros de validação do serviço.
        let errors = error.data.errors;
        mostrarErrosValidacao(errors);
      });
  };

  let cadastrarEmpresa = function(empresa) {
    empresaApi.cadastrar(empresa)
      .then(function(response) {

        // Limpar formulário.
        limparFormulario();

        // Redirecionamento de página.
        $state.transitionTo('empresas', {
          reload: true,
          inherit: false,
          notify: true
        });

        // Caixa de confirmação - Toast
        var toast = $mdToast.simple()
          .textContent('A empresa foi cadastrada com sucesso!')
          .position('top right')
          .action('OK')
          .hideDelay(6000);
        $mdToast.show(toast);
      })
      .catch(function(error) {
        // Exibir erros de validação do serviço.
        let errors = error.data.errors;
        mostrarErrosValidacao(errors);
      });
  }

  let mostrarErrosValidacao = function(errors) {
    for (mensagem of errors) {
      var toast = $mdToast.simple()
        .textContent(mensagem)
        .position('top right')
        .action('OK')
        .hideDelay(6000);
      $mdToast.show(toast);
    }
  }

  let limparFormulario = function() {

    // Reinicializa a variável empresa.
    angular.copy({}, $scope.empresa);

    // Reinicializa o estado do campo para os eventos e validação.
    // É necessário indicar o atributo name no formulário <form>
    $scope.empresaForm.$setPristine();
    $scope.empresaForm.$setUntouched();
    $scope.empresaForm.$setValidity();
  }
}

app.controller('EmpresaController', empresaController);
