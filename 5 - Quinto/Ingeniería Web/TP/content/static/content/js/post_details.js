var commentHtml;
var myRating;
        
$(document).ready(function() {
    commentHtml = $('#comment-post').parent().html();

    // Configuración del componente Rating.
    var el = document.querySelector('#star-rating');
    if (el) {
        var currentRating = $('#current-user-rating').val();
        var maxRating= 10;
        postId = $('#post-id').val();
        var callback = function(rating) { votePost(rating, postId); };
        myRating = rating(el, currentRating, maxRating, callback);

        // Configuración de Tooltips para el componente Rating.
        $('li.c-rating__item').each(function() {
            stars = parseInt($(this).attr('data-index')) + 1;
            text = ' estrella';
            if (stars > 1) {
                text+='s'
            }
            tooltipText = stars + text;

            $(this).attr('data-original-title', tooltipText).attr('data-toggle', 'tooltip').attr('data-placement', 'top');
        });
    }

    // Inicializar Tooltips.
    $('[data-toggle=tooltip]').tooltip();

});

function respondTo(element, postId) {
    deleteCommentBoxes();
    $(element).parent().parent().append(commentHtml);

    $('#id_response_to_id').val(postId);
    
    configureSummernoteComponent();
    
    return false;
}

function reportTo(contentId) {
    $('#id_content_id').val(contentId);
    
    $("#report-confirmation").modal();

    return false;
}

function ajaxReport() {
    $.ajax({
        url: '/ajax_complaint',
        type: 'POST',
        data: $("#complaint-form").serialize(),
        success: function(data) {
            $("#report-result-title").html(data.title);
            $("#report-result-description").html(data.description);

            // Resetear formulario para borrar el contenido ingresado.
            $("#complaint-form").trigger("reset");
        },
        error: function(){
            $("#report-result-title").html('Error');
            $("#report-result-description").html('Se produjo un error al reportar el contenido. Por favor, inténtalo nuevamente.');
        },
        complete: function() {
            $("#report-result").modal();
        }
    });

    return false;
}

function votePost(rating, postId) {
    $.ajax({
        url: '/ajax_vote_post',
        type: 'POST',
        data: { rating: rating, post_id: postId },
        cache: false,
        success: function(data) {
            if (data.success) {
                $('#post-rating').html(data.new_score);
                $('#post-vote-count').html(data.vote_count);
            }
            else {
                alert('Hubo un error al procesar su votación. Inténtelo nuevamente.');
            }
        },
        error: function() {
            alert('Hubo un error al procesar su votación. Inténtelo nuevamente.');
        },
    });
}

function deleteCommentBoxes() {
    $('#comment-post').remove();
    $('#edit-comment').remove();
}

function restaurarComentario(){
    deleteCommentBoxes();
    $('#comment-post-container').append(commentHtml);
    
    configureSummernoteComponent();
    
    return false;
}

function configureSummernoteComponent(textToInsert = ''){
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
        placeholder: 'Escribí un comentario...',
    });
    $('#summernote').summernote('code', textToInsert);
}

function deleteVote() {
    myRating.setRating('0');
}

function showCommentDeleteConfirmation(commentId) {
    $('#delete-comment-id').val(commentId);

    $("#delete-comment-confirmation").modal();

    return false;    
}

function favPost(postId) {
    $.ajax({
        url: '/ajax_favorite',
        type: 'POST',
        data: { post_id: postId },
        cache: false,
        success: function(data) {
            if (data.success) {
                if (data.fav) {
                    $('#fav-heart').css('animation', 'grayToRed 1s ease 1').css('animationFillMode', 'forwards').attr('data-original-title', 'Quitar de favoritos');
                }
                else {
                    $('#fav-heart').css('animation', 'redToGray 1s ease 1').css('animationFillMode', 'forwards').attr('data-original-title', 'Marcar como favorito');
                }
            }
            else {
                alert('Ha ocurrido un error. Inténtelo nuevamente.');                
            }
        },
        error: function() {
            alert('Ha ocurrido un error. Inténtelo nuevamente.');
        },
    });

    return false;
}

function editComment(commentId) {
    // Obtener comentario original.
    var originalComment = $('#comment-' + commentId).html()

    // Eliminar otras cajas de comentarios.
    deleteCommentBoxes();

    // Obtener template para editar comentario.
    var template = '';
    $.get('/_edit_comment.html/', function(data) {
        template = data; 

        // Configurar template con el id del comentario a editar.
        template = template.replace('%comment-id%', commentId);

        // Colocar template bajo el comentario a editar.
        $('#comment-' + commentId).parent().append(template);
        
        // Configurar componente de Summernote y agregar comentario original.
        configureSummernoteComponent(originalComment);
    });
    
    return false;
}