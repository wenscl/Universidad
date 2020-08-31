// Mantener la tab activa actualmente al refrescar la página.
$('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
    localStorage.setItem('activeTab', $(e.target).attr('href'));
});
var activeTab = localStorage.getItem('activeTab');
if(activeTab){
    $('.nav-tabs a[href="' + activeTab + '"]').tab('show');
}


// Mantener el collapse al refrescar la página.
$(document).ready(function () {
    $('a[data-toggle="collapse"]').click(function() {
        //store the id of the collapsible element
        localStorage.setItem('collapseItem', $(this).attr('href'));
    });

    var collapseItem = localStorage.getItem('collapseItem'); 
    if (collapseItem) {
       $(collapseItem).collapse('show')
    }
})

// // Cambiar el icono cuando se colapsa y descolapsa el filtro.
// $(document).ready(function () {
//     $('.collapse')
//         .on('shown.bs.collapse', function() {
//             $(this)
//                 .parent()
//                 .find(".fa-angle-up")
//                 .removeClass("fa-angle-up")
//                 .addClass("fa-angle-down");
//         })
//         .on('hidden.bs.collapse', function() {
//             $(this)
//                 .parent()
//                 .find(".fa-angle-down")
//                 .removeClass("fa-angle-down")
//                 .addClass("fa-angle-up");
//         });
//     });


// $('.navbar-dark .navbar-nav a').on('click', function () {
// 	$('.navbar-nav').find('a.active').removeClass('active');
// 	$(this).addClass('active');
// });