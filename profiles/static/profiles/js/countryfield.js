let counrtySelected =  $('#id_default_country').val();
if(!counrtySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function(){
    counrtySelected = $(this).val();
    if(!counrtySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});