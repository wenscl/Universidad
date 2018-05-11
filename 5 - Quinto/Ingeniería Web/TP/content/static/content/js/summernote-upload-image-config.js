// Función para subir las imágenes de Summernote mediante AJAX.
function upload_image(files) {
    for (var i = 0, len = files.length; i < len; i++) {
        var data = new FormData();
        data.append('image', files[i]);
        $.ajax({
            url: '/ajax_upload_image',
            type: 'POST',
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data.success){
                    $('#summernote').summernote('insertImage', data.url, data.filename);
                }
                else{
                    alert('Se produjo un error al cargar la imagen. Por favor, inténtalo nuevamente.');
                }
            },
            error: function(){
                alert('Se produjo un error al cargar la imagen. Por favor, inténtalo nuevamente.');
            }
        });
    }
};