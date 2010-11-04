$(document).ready(function(){
    $("#accordion").accordion();
    $("#tab_content").css('height', $("#accordion").css('height'));
    $(".accordion_link").click(function() {
        $.ajax({
            url: $(this).attr('id'),
            type: 'get',
            success: function(data) {
                $("#tab_content").html(data)
            },
            dataType: 'text'
        });
    });
});
