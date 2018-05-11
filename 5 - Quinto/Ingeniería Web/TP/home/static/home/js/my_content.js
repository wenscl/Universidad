function goToPage(pageNumber, isPublished, isDeleted, isList) {
    element = '';
    if (isPublished) {
        if (isList) {
            element = $('#published-content-list');
        }
        else {
            element = $('#published-content-post');        
        }
    }
    else {
        if (isList) {
            element = $('#draft-content-list');
        }
        else {
            element = $('#draft-content-post');        
        }
    }
    if (isDeleted) {
        element = $('#recicle-bin-list');
    }

    element.fadeOut(250, function() {
        $.ajax({
            url: '/ajax_profile_posts_list',
            type: 'POST',
            data: { page_number: pageNumber, is_published: isPublished, is_deleted: isDeleted, is_list: isList },
            cache: false,
            success: function(data) {
                if (data.success) {
                    element.html(data.html);
                }
                else {
                    alert('Hubo un error al recuperar la lista de posts.');            
                }
            },
            error: function(){
                alert('Hubo un error al recuperar la lista de posts.');
            },
        });
        element.fadeIn(250);
    });
    
    return false;
}