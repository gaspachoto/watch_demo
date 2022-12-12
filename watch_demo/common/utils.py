def get_movie_url(request, movie_id):
    return request.META['HTTP_REFERER'] + f'#photo-{movie_id}'