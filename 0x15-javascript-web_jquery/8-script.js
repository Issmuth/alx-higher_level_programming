$(function() {
    let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    fetch(url).then(response => response.json()).then(result => {
        data = result;
        movieList = data.results;
	movieList.forEach(function (movie) {
            $('UL#list_movies').append('<li>'+ movie.title + '</li>');
        });
    });
});
