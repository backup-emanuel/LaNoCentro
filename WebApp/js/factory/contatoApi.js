// Empresas - Factory
var contatoFactory = function($http, serviceCfg) {

  var baseUrl = serviceCfg.baseUrl();

  var _cadastrar = function(empresa) {
    return $http.post(baseUrl + "/contatos", empresa);
  };

  var _listar = function() {
    return $http.get(baseUrl + "/contatos");
  };

  var _pesquisarPorId = function(id) {
    return $http.get(baseUrl + "/contatos/" + encodeURI(id));
  };

  var _buscarPorNome = function(nome) {
    return $http.get(baseUrl + "/contatos/nome/" + encodeURI(nome));
  }

  return {
    cadastrar: _cadastrar,
    listar: _listar,
    pesquisarPorId: _pesquisarPorId,
    buscarPorNome: _buscarPorNome
  };
}

app.factory("contatoApi", contatoFactory);
