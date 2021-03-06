$(document).ready(function(){
    $("#accordion").accordion();

    $("#main_content").css('height', $("#accordion").height());

    $(".accordion_link").click(function() {
        $.ajax({
            url: $(this).attr('id'),
            type: 'get',
            success: function(data) {
                $("#main_content").html(data)
            },
            error: function(xhr, text, err) {
                $("#main_content").html(xhr.responseText);
            },
            dataType: 'text'
        });
    });
});
