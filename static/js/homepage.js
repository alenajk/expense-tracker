$('.checkbox').click(function(){
    var cat = $(this).attr('value');
    if ($(this).attr('checked')){
        $('.'+cat).hide()
        $(this).attr('checked',false)
    } else {
        $(this).attr('checked',true)
        $('.'+cat).show()
    };
});