from django.contrib import admin

from watch_demo.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'year_of_release')

    # @staticmethod
    # def pets(current_photo_obj):
    #     tagged_pets = current_photo_obj.tagged_pets.all()
    #     if tagged_pets:
    #         return ', '.join(p.name for p in tagged_pets)
    #     return 'No pets'
