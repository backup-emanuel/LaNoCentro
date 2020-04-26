/*
 *  Converter valores booleanos (true ou false) para Sim ou Não nos DataTables.
 */
app.filter('yesNo', function() {
    return function(input) {
        return input ? 'Sim' : 'Não';
    }
});
