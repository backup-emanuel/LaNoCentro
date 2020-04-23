// Empresas - Factory
var cidadeFactory = function($http, serviceCfg) {

  var baseUrl = serviceCfg.baseUrl();

  var _listar = function() {
    return $http.get(baseUrl + "/cidades");
  };

  var _pesquisarPorId = function(id) {
    return $http.get(baseUrl + "/cidades/" + encodeURI(id));
  };

  return {
    listar: _listar,
    pesquisarPorId: _pesquisarPorId
  };
}

app.factory("cidadeApi", cidadeFactory);
