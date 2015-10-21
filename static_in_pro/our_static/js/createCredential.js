$(document).ready(function(){
    if ($('#id_keyOrPassword_0').prop("checked")){
        showPassword()
    }
});

$('#id_keyOrPassword_0').on("click", function(){
    showPassword()
});

$('#id_keyOrPassword_1').on("click", function(){
    hidePassword()
});

function hidePassword(){
    $('#id_password').parent().addClass('hidden')
    $('#id_username').parent().addClass('hidden')
}

function showPassword(){
    $('#id_username').parent().removeClass("hidden")
    $('#id_password').parent().removeClass("hidden")
}
