$(function() {
    let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    fetch(url).then(response => response.json()).then(result => {
        $('DIV#hello').text(result.hello);
    });
});
