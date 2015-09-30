/**
 * Created by dborysenko on 9/30/2015.
 */
$(document).ready(function () {
    var pathname = window.location.pathname;
    console.log(pathname)
    if (pathname.indexOf('projects') == 1) {
        $('#Projects').attr('class', 'active')
    }else if (pathname.indexOf('inventories') == 1){
        $('#Inventories').attr('class', 'active')
    }else if (pathname.indexOf('jobtemplates') == 1){
        $('#JobTemplates').attr('class', 'active')
    }else{
        $('#Home').attr('class', 'active')
    }
});
