$(document).ready(function() {
    // Configuración del componente Summernote.
    $('#summernote').summernote({
        height: 300,
        dialogsFade: true,
        lang: 'es-ES',
        callbacks: {
            onImageUpload: function(files) {
                upload_image(files);
            }
        },
        toolbar: [
            // [groupName, [list of button]]
            ['Estilo', ['style', 'bold', 'italic', 'underline', 'color', 'clear']],
            ['Fuente', ['fontname', 'fontsize']],
            ['Párrafo', ['ul', 'ol', 'paragraph', 'height']],
            ['Insertar', ['link', 'picture', 'video', 'table', 'hr']],
            ['Otros', ['undo', 'redo', 'codeview', 'help']]
        ],
        placeholder: 'Escribí algo interesante...'
    });

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