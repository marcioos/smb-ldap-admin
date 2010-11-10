$(document).ready(function(){
    $("#accordion").accordion();
    $("#main_content").css('height', $("#accordion").css('height'));
    $(".accordion_link").click(function() {
        $.ajax({
            url: $(this).attr('id'),
            type: 'get',
            success: function(data) {
                $("#main_content").html(data)
            },
            dataType: 'text'
        });
    });
});
