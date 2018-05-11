$(document).ready(function() {
    // Configuración del AutoComplete para Películas y Series.
    var moviesAndTvShows = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        remote: {
            url: '/item_suggestion/?query=%QUERY',
            wildcard: '%QUERY'
        }
    });

    $('.itemInput').typeahead(null, {
        name: 'moviesAndTvShows',
        display: function(suggestion) {
                return '';
            },
        source: moviesAndTvShows,
        templates: {
            empty: [
            '<div class="empty-message">',
                'No se han encontrado películas que coincidan con su búsqueda',
            '</div>'
            ].join('\n'),
            suggestion: function(suggestion) {
                return '<div><strong>' + suggestion.name + '</strong> (' + suggestion.year + ') <small>[' + suggestion.type_verbose + ']</small></div>';
            },
        },
    });
    
    $('.itemInput').bind('typeahead:select', function(ev, suggestion) {
        // Al seleccionar una sugerencia, se agrega una nueva fila a la tabla.
        $('#itemList tbody').append(
            '<tr><td>' + suggestion.name + ' (' + suggestion.year + ')</td><input type="hidden" name="item" value="' + suggestion.id + ':' + suggestion.type + '"><td>' + suggestion.type_verbose + '</td><td class="text-center"><i class="fa fa-arrow-up move-row" onclick="return moveRow(this, \'up\');" title="Mover hacia arriba"></i></td><td class="text-center"><i class="fa fa-arrow-down move-row" onclick="return moveRow(this, \'down\');" title="Mover hacia abajo"></i></td><td class="text-center"><i class="fa fa-times delete-row" onclick="return deleteRow(this);" title="Quitar"></i></td></tr>'
        );

    });

    // Antes de realizar el submit, se establece el valor a "items-list" con los items de la tabla.
    $('#content-form').submit(function() {
        var itemList = $('[name="item"]').map(function() {
            return $( this ).val();
        })
        .get()
        .join( "," );

        $('#items-list').val(itemList);
    })
});

function deleteRow(element){
    $(element).parent().parent().remove();

    return false;
}

function moveRow(element, direction) {
    var rowToMove = $(element).parent().parent();
    var rowContent = rowToMove.prop('outerHTML');
    
    if (direction == 'up') {
        var previousRow = rowToMove.prev();
        if (previousRow.length) {
            previousRow.before(rowContent);
            rowToMove.remove();
        }
    }
    else {
        var nextRow = rowToMove.next();
        if (nextRow.length) {
            nextRow.after(rowContent);
            rowToMove.remove();
        }
    }

    return false;
}