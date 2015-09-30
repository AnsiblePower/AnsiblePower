/**
 * Created by dborysenko on 9/29/2015.
 */
//$( document ).ready(function(){
//    $("#navbarid li").click(function(){
//        $("#navbar li").removeClass("active");
//        $(this).addClass("active");
//    });
//});
//$('[data-toggle=confirmation]').confirmation({popout: true});
//$('#deleteProject').confirmation();
//$('#deleteconfirm').on('show.bs.modal', function (event) {
//  var button = $(event.relatedTarget) // Button that triggered the modal
//  var pk = button.data('pk') // Extract info from data-* attributes
//  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
//  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
//  var modal = $(this)
//    console.log(pk)
//  //modal.find('.modal-title').text('New message to ' + recipient)
//  modal.find('deleteconfirmbutton').attr("id", "deleteconfirm".concat(pk))
//})

//$('#deleteconfirm').on('show.bs.modal', function(e) {
//    var button = $(e.relatedTarget )
//    var pk = button.data('pk')
//    var btn = $(this).find('.btn-ok')
      //btn.click({'pk': pk}, confirmProjectDelete)
//});

$("button[id^='deleteprojectbutton']").click(function () {
    var modalwindow = $('#deleteconfirmmodal').modal('show')
    var pk = $(this).data('pk')
    var name = $(this).data('name')
    modalwindow.find('.modal-body').append(name)
    var okbtn = modalwindow.find('.btn-ok')
    okbtn.click({'pk': pk}, confirmProjectDelete)
})


function confirmProjectDelete(event) {
    var pk = event.data.pk
    console.log('Working here...')
    console.log(pk)
    $.ajax({
        type: "POST",
        url: "/projects/deleteproject/".concat(pk).concat('/'),
        dataType: "json",
        data: {"item": $(".todo-item").val()},
        success: function (data) {
            alert(data.message);
        }
    });
    $('#row'.concat(pk)).collapse('hide')
    $('#deleteconfirmmodal').modal('hide')
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