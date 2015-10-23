var showpuPublickKey = $('#showpublickkey')
showpuPublickKey.on("click", function(){
    var credID = $('#id_credentials option:selected').val()
    if ( !showpuPublickKey.attr('aria-describedby')) {
        $.get("/inventories/showpubkey/".concat(credID).concat("/"), function( data ){
            console.log(data.pubkey);
            showpuPublickKey.popover({'content': data.pubkey})
            showpuPublickKey.popover('show')
        })
    }else{
        showpuPublickKey.popover('hide')
    }

});

//$(function () {
//  $('[data-toggle="popover"]').popover()
//});

