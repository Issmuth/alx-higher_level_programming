$(function() {
    let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    fetch(url).then(response => response.json()).then(result => {
   	data = result;
	$('DIV#character').html(data.name);
    });
});
