function showConfirmBanModal() {
    $("#confirm-ban").modal();
}

function showCancelBanModal() {
    $("#cancel-ban").modal();
}

function showCancelUserBanModal(userCancelBanUrl) {
    $("#cancel-user-ban-button").attr("href", userCancelBanUrl);
    $("#cancel-user-ban").modal();
    
    return false;
}

function goToPage(pageNumber, type) {
    element = '';
    if (type == 'post') {
        element = $('#reported-posts-list');
    }
    else if (type == 'comment' ) {
        element = $('#reported-comments-list');
    }
    else {
        element = $('#banned-users-list');        
    }

    element.fadeOut(250, function() {
        $.ajax({
            url: 'ajax_moderation_pagination',
            type: 'POST',
            data: { page_number: pageNumber, type: type },
            cache: false,
            success: function(data) {
                if (data.success) {
                    element.html(data.html);
                }
                else {
                    alert('Hubo un error al recuperar la lista.');            
                }
            },
            error: function(){
                alert('Hubo un error al recuperar la lista.');
            },
        });
        element.fadeIn(250);
    });
    
    return false;
}