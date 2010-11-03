$(document).ready(function(){
    $("#accordion").accordion();
    $("#actions").css('height', $("#accordion").css('height'));
    $(".accordion_link").click(function() {
        $.ajax({
            url: $(this).attr('name'),
            type: 'get',
            success: function(data) {
                $("#actions").html(data)
            },
            dataType: 'text'
        });
    });
});
