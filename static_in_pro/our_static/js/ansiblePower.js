/**
 * Created by dborysenko on 9/30/2015.
 */
$(document).ready(function () {
    var pathname = window.location.pathname.split('/')[1];
    if (pathname == ''){
        $('#home').attr('class', 'active')
    }else{
        $('#' + pathname).attr('class', 'active')
    }
});
