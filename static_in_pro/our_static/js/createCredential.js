$(document).ready(function(){
    //hidePassword()
    $(".has-error").removeClass("hidden")
    $(".has-success").removeClass("hidden")
});

$('#id_keyOrPassword_0').on("click", function(){
    showPassword()
});

$('#id_keyOrPassword_1').on("click", function(){
    hidePassword()
});

function hidePassword(){
    $('#id_username').parent().attr('class', 'hidden')
    $('#id_password').parent().attr('class', 'hidden')
}

function showPassword(){
    $('#id_username').parent().attr('class', '')
    $('#id_password').parent().attr('class', '')
}