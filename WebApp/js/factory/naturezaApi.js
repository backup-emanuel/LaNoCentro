// Empresas - Factory
var naturezaFactory = function($http, serviceCfg) {

  var baseUrl = serviceCfg.baseUrl();

  var _listar = function() {
    return $http.get(baseUrl + "/naturezas");
  };

  var _pesquisarPorId = function(id) {
    return $http.get(baseUrl + "/naturezas/" + encodeURI(id));
  };

  return {
    listar: _listar,
    pesquisarPorId: _pesquisarPorId
  };
}

app.factory("naturezaApi", naturezaFactory);
