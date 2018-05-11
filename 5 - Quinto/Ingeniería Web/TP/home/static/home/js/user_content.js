function goToPage(userId, pageNumber, isList) {
    element = '';
    if (isList) {
        element = $('#published-content-list');
    }
    else {
        element = $('#published-content-post');        
    }
    
    element.fadeOut(250, function() {
        $.ajax({
            url: '/ajax_user_profile_posts_list',
            type: 'POST',
            data: { user_id: userId, page_number: pageNumber, is_list: isList },
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