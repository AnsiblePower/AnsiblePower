/**
 * Created by dborysenko on 9/29/2015.
 */

$("button[id^='deletebutton']").click(function () {
    var modalwindow = $('#deleteconfirmmodal').modal('show');
    var pk = $(this).data('pk');
    var name = $(this).data('name');
    var postTarget = $(this).data('posttarget');
    modalwindow.find('.modal-body').html(name);
    var okbtn = modalwindow.find('.btn-ok');
    okbtn.click(function(){
        confirmDelete(pk, postTarget);
    })
});

$("#id_project").change(function(){
    var projID = $('#id_project option:selected').attr('value');
    console.log(projID);
    $.get("/jobtemplates/getjsondirectory/".concat(projID), function(data){
        //console.log(data.directory)
        $.each(data, function(k, v){
            //console.log(v)
            $('#id_playbook').append($("<option></option")
                .attr("value", v)
                .text(v));
        })
    })
});

function handleError(textStatus) {
    console.log(textStatus)
    $('#deleteconfirmmodal').modal('hide')
}

function handleSuccess(successObj){
    $('#row'.concat(pk)).collapse('hide');
    $('#deleteconfirmmodal').modal('hide')
}

function confirmDelete(pk, postTarget) {
    $.ajax({
        type: "POST",
        url: postTarget.concat(pk).concat('/'),
        dataType: "json",
        data: {"item": $(".todo-item").val()},
        success: function (data) {
            handleSuccess(data)
        },
        error: function (textStatus) {
            handleError(textStatus)
        }
    });
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    var i = 0;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
$.ajaxSetup({

    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
