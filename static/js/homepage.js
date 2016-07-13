$('.checkbox').click(function(){
    var cat = $(this).attr('value');
    if ($(this).attr('checked')){
        // $('.'+cat).hide()
        $('.'+cat).addClass('hidden');
        $(this).attr('checked',false)
    } else {
        $(this).attr('checked',true)
        // $('.'+cat).show()
        $('.'+cat).removeClass('hidden');
    };
    get_total();
});

function get_total() {
    var activeExpenses = $('.expense').not('.hidden');
    var total = 0;
    $.each(activeExpenses, function(activeExpense) {
        var amount = $(this).children().children('.amount')[0].innerText;
        amount = parseInt(amount.slice(1));
        total = total + amount;
    });
    $("#total").html(total);
}

$(document).ready(function(){
    get_total();    
});
