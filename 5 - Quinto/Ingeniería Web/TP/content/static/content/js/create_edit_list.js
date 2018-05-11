$(document).ready(function() {
    // Configuración del componente Select2.
    $('#tagsinput').select2({
        language: "es",
        tags: true,
        placeholder: "Ingresá los tags deseados...",
        maximumSelectionLength: 10,
        ajax: {
            url: "/ajax_tag_suggestions",
            data: function (params) {
                return {
                    q: params.term,
                };
            },
            processResults: function (data, params) {
                return {
                    results: data,
                };
            },
            dataType: 'json',
            delay: 250,
            cache: true,
        },
        minimumInputLength: 1,
    });

    // Agregar los tags preexistentes.
    if (tag_list) {
        tag_list.split(',').forEach(function(tag) {
            $('#tagsinput').append(
                $('<option></option>').attr('selected','selected').attr('value', tag).text(tag)
            );
        });
    }
});