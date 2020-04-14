// Empresas - Factory
var empresaFactory = function($http) {

  var baseUrl = "http://127.0.0.1:5000";

  var _cadastrar = function(empresa) {
    return $http.post(baseUrl + "/empresa", empresa);
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
