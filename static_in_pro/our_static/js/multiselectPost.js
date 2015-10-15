/**
 * Created by dborysenko on 10/15/2015.
 */

$(document).ready(function(){
    var s1 = document.getElementsByName('hosts')[0];
    for (var i = 0; i < s1.options.length; i++) {
        s1.options[i].selected = false;
    }
});

jQuery(document).ready(function ($) {
    $('#search').multiselect({
        search: {
            left: '<input type="text" name="q" class="form-control" placeholder="Search..." />',
            right: '<input type="text" name="q" class="form-control" placeholder="Search..." />',
        }
    });
});
$('#saveMultiselect').on('click', function (event) {
    var s1 = document.getElementsByName('hosts')[0];
    for (var i = 0; i < s1.options.length; i++) {
        s1.options[i].selected = true;
    }
});
