$(document).ready(function(){
    //hidePassword()
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
    $('#id_username').removeAttr('required')
    $('#id_password').removeAttr('required')
}

function showPassword(){
    $('#id_username').parent().attr('class', '')
    $('#id_password').parent().attr('class', '')
    $('#id_username').attr('required', 'required')
    $('#id_password').attr('required', 'required')
}