# Movie Database - Web Project

The aim of our project is to build a website where people can find movie recommendations based on their favourite actor/director/category, so the Topic will be Movie recommendation.
We’ll use themoviedb API that contains a movie database with Entities such as Movies, People(Actors/directors), Genres etc.
We will have five entities being them Movie, People, Genre, Categories and Casting,
where the last two will be the relation between Movie & Genre and Movie & People
respectively.

## Getting Started

If you want to run the website in your local machine for developing and testing you
have to get a project copy.
To clone the repository you have to download it to your computer.


### Prerequisites

To use the project you have to install the "requirements.txt" located in the project repository.
Use the following command:

```
pip install -r requirements.txt
```

### Installing

To run and check the website functionality you have to follow the next steps:

**1. Open the project folder.**

**2. Run the server**
```
python manage.py runserver
```
 **3. Open the web browser.**

 **4. Search for: 127.0.0.1:8000 .**

## Docker pull image

To download the docker image you can use the following command:

```
docker pull mjunyent/skeleton
```

To run the image in a container use the command:

```
docker run --name test -it mjunyent/skeleton
```

## Heroku website

To watch the website you can use the following link:

* [Click here](https://movie-db-web-project.herokuapp.com/)

## Add API information

In order to add the API information to the local database you have to visit the following website:

* [API](http://127.0.0.1:8000/readapi) - Download API information

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Movie API](https://www.themoviedb.org/documentation/api) - API used in the project
* [Bootstrap](https://getbootstrap.com/) - It contains CSS templates

## Authors

* **Boris Llona** [borisllona](https://github.com/borisllona)
* **Hatice Hüma Kalaycı** [humoshi](https://github.com/humak)
* **Mateus Martins** [mateusdaemon](https://github.com/mateusdaemon)
* **Atakan Göl** [atakangol](https://github.com/atakangol)
* **Marc Junyent** [jumo9999](https://github.com/jumo9999)

See also the list of [contributors](https://github.com/atakangol/webProjectMovieDB/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Development considerations

For the template design we use a base.html, where we put the navbar and its style, using css, bootstrap and crispy forms.
For extend the same layout in the others page, we use the content logic, then for it template we extend the style from the base.html file.
For the login and register, we use the Django forms, this way is much easier because Django already does everything for you, and also take care of password and username logic.
All the css we use, we have decided to out in a folder called Static, and to be able to use in the heroku platform, as Django is not capable of handle the static files in production, we use the whitenoise app, and than set the URL for static files and its root. This way, the page in production is able of find de CSS style, otherwise wouldn't work.
