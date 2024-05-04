$('DIV#toggle_header').on('click', function() {
    if ($('header').is('.red')) {
	$('header').removeClass('red');
        $('header').addClass('green');
    } else {
        $('header').removeClass('green');
        $('header').addClass('red');
    }
});
