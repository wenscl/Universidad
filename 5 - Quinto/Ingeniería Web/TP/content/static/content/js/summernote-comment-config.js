$(document).ready(function() {
    // Configuración del componente Summernote.
    $('#summernote').summernote({
        height: 150,
        dialogsFade: true,
        lang: 'es-ES',
        callbacks: {
            onImageUpload: function(files) {
                upload_image(files);
            }
        },
        toolbar: [
            ['Estilo', ['style', 'bold', 'italic', 'underline', 'color',]],
            ['Fuente', ['fontname', 'fontsize',]],
            ['Párrafo', ['ul', 'ol',]],
            ['Insertar', ['link', 'picture', 'video',]],
        ],
        placeholder: 'Escribí un comentario...'
    });
});