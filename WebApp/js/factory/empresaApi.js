// Empresas - Factory
var empresaFactory = function($http, serviceCfg) {

  var baseUrl = serviceCfg.baseUrl();

  var _cadastrar = function(empresa) {
    return $http.post(baseUrl + "lanocentro/api/empresas", empresa);
  };

  var _listar = function() {
    return $http.get(baseUrl + "/empresas");
  };

  var _pesquisarPorId = function(id) {
    return $http.get(baseUrl + "/empresas/" + encodeURI(id));
  };

  return {
    cadastrar: _cadastrar,
    listar: _listar,
    pesquisarPorId: _pesquisarPorId
  };
}

app.factory("empresaApi", empresaFactory);
