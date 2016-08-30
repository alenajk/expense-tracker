$('.checkbox').click(function(){
    var cat = $(this).attr('value');
    if ($(this).attr('checked')){
        $('.'+cat).addClass('hidden');
        $(this).attr('checked',false)
    } else {
        $(this).attr('checked',true)
        $('.'+cat).removeClass('hidden');
    };
    get_total();
});

function get_total() {
    var activeExpenses = $('.expense').not('.hidden');
    var total = 0;
    $.each(activeExpenses, function(activeExpense) {
        var amount = $(this).children().children('.amount')[0].innerText;
        amount = parseFloat(amount.slice(1));
        total = total + amount;
    });
    $("#total").html('$' + String(total));
};

$(document).ready(function(){
    get_total();    
});

$(function() {
 $( "#datepicker" ).datepicker();
 $( "#datepicker2" ).datepicker();
});

var isAfter = function(startDate, endDate){
    var start = moment(0);
    var end = moment();

    if (endDate){
        end = moment(endDate);
    };
    if (startDate){
        start = moment(startDate);
    };

    return end > start;
};

$('#filter-button').click(function(){   
    var ex = $('.expense .upper-bar .date');
    $.each(ex, function(ex) {
        var expenseDate = $(this).text();
        var startDate = String($('#datepicker').datepicker('getDate'));
        var endDate = String($('#datepicker2').datepicker('getDate'));
        if (isAfter(expenseDate, startDate) || isAfter(endDate, expenseDate)){
            // hide expense entry if before startDate or after endDate
            $(this).parent().parent().addClass('hidden');
        } else {
            if ($(this).parent().parent().hasClass('hidden')){
                $(this).parent().parent().removeClass('hidden');
            }; 
        };
    });
    toggleCheckboxes(getActiveCategories());
    get_total();
});

function getActiveCategories(){

    var activeExpenses = $('.expense').not('.hidden');
    var activeCategories = []
    
    // Iterate over active expenses, push category to activeCategories
    $.each(activeExpenses, function(activeExpenses) {
        var category = $(this).find('.category')[0].innerHTML;
        if ($.inArray(category, activeCategories) == -1) {
            activeCategories.push(category);            
        }
    });
    return activeCategories;
}

function toggleCheckboxes(activeCategories){
    $.each($('.checkbox-span'), function(i, val) {
        if ($.inArray(val.innerText, activeCategories) == -1) {
            $(this).addClass('hidden');
        }else {
            $(this).removeClass('hidden');
        }
    })
}
