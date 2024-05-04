#!/usr/bin/node
$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
        let url = 'https://www.fourtonfish.com/hellosalut/?lang=' +  $('INPUT#language_code').val();
	console.log(url);
	$.get(url + + $.param({ lang: $('INPUT#language_code').val() }), function(result) {
            $('DIV#hello').text(result.hello);
        });
    });
});
