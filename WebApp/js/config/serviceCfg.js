/*
 *  Configuração de conexão de serviço.
 */
app.value("serviceCfg", {

	baseUrl: function() {

		var _protocol = "//"
		var _hostAddress = "localhost";
		var _port = "5000";
		var _context = "/lanocentro/api";

		return _protocol + _hostAddress + ":" + _port + _context;
	}

})
