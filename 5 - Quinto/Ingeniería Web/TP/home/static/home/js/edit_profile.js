$(document).ready(function() {
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
        autoclose: true,
        clearBtn: true,
        endDate: '0d',
        language: 'es',
        startView: 'decades'
    });
});