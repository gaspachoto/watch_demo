from django.contrib.auth import get_user_model

from watch_demo.movies.models import Movie

UserModel = get_user_model()


def create_movies_for_user(user, count=5):
    result = [Movie(
        name=f'Movie',
        genre=f'Horror',
        movie_poster=f'C://movies.com.jpg',
        year_of_release='2001',
        description='descriptiondescriptiondescription',
        user=user
    ) for i in range(count)]

    [m.save() for m in result]

    return result


def create_movie_for_user(user):
    movie = Movie(
        name=f'Test_movie',
        genre=f'Horror',
        movie_poster=f'C://movies.com.jpg',
        year_of_release='2001',
        description='descriptiondescriptiondescription',
        user=user
    )
    movie.save()
    return movie