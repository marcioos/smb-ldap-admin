$(document).ready(function() {
    var bigger_width = 0;
    $('label').each(function() {
        var width = parseInt($(this).css('width'));
        if(width > bigger_width)
            bigger_width = width;
    });
    $('label').css('width', bigger_width);
    $('.div_textbox').css('margin-left', bigger_width + 15);
});
