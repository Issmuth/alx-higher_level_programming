#!/usr/bin/node
$(document).ready(function() {
    function translate(){
        let url = 'https://www.fourtonfish.com/hellosalut/?';
	$.get(url + + $.param({ lang: $('INPUT#language_code').val() }), function(result) {
            $('DIV#hello').text(result.hello);
        });
    }

    $('INPUT#btn_translate').click(translate);
    $('INPUT#language_code').keypress(function() {
        let keycode = (event.keyCode ? event.keyCode: event.which);
	if(keycode == '13') {
		translate();
	}
    });
});
