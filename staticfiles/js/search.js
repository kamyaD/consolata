$('#createModal').on('shown.bs.modal', function() {
    $('.js-example-basic-multiple').select2({
        width: '100%',
        placeholder: 'Start Typing...',
        dropdownParent: $('#createModal')
    }).on('select2:open', function() {
        $('.select2-dropdown').css('z-index', 99999);
    });
});

$('#createModal').on('shown.bs.modal', function() {
    $('.js-example-basic-single').select2({
        width: '100%',
        dropdownParent: $('#createModal')
    }).on('select2:open', function() {
        $('.select2-dropdown').css('z-index', 99999);
    });
});
