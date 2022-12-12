def calculate_rating(movie):
    movie_rating_count = movie.movierating_set.count()
    if movie_rating_count == 0:
        return f'Not rated yet!'
    total_rating_values = movie.movierating_set.values_list('rating')
    total_ratings = [sum(x) for x in total_rating_values]
    total_rating = sum(int(x) for x in total_ratings) / movie_rating_count
    return f'{total_rating:.1f}'