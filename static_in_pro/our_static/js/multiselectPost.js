/**
 * Created by dborysenko on 10/15/2015.
 */

$(document).ready(function () {
    var s1 = document.getElementsByName('hosts')[0];
    if (s1) {
        for (var i = 0; i < s1.options.length; i++) {
            s1.options[i].selected = false;
        }
    }
    var s2 = document.getElementsByName('groups')[0];
    if (s2) {
        for (var j = 0; j < s2.options.length; j++) {
            s2.options[j].selected = false;
        }
    }
});

jQuery(document).ready(function ($) {
    $('#HostSearch').multiselect({
        search: {
            left: '<input type="text" name="q" class="form-control" placeholder="Search..." />',
            right: '<input type="text" name="q" class="form-control" placeholder="Search..." />',
        }
    });
    $('#GroupSearch').multiselect({
        search: {
            left: '<input type="text" name="q" class="form-control" placeholder="Search..." />',
            right: '<input type="text" name="q" class="form-control" placeholder="Search..." />',
        }
    });
});
$('#saveMultiselect').on('click', function (event) {
    var s1 = document.getElementsByName('hosts')[0];
    if (s1) {
        for (var i = 0; i < s1.options.length; i++) {
            s1.options[i].selected = true;
        }
    }
    var s2 = document.getElementsByName('groups')[0];
    if (s2) {
        for (var j = 0; j < s2.options.length; j++) {
            s2.options[j].selected = true;
        }
    }
});
