// Empresas - Factory
var estadoFactory = function($http, serviceCfg) {

  var baseUrl = serviceCfg.baseUrl();

  var _listar = function() {
    return $http.get(baseUrl + "/estados");
  };

  var _pesquisarPorId = function(id) {
    return $http.get(baseUrl + "/estados/" + encodeURI(id));
  };

  return {
    listar: _listar,
    pesquisarPorId: _pesquisarPorId
  };
}

app.factory("estadoApi", estadoFactory);
