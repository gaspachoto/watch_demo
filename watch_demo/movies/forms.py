from django import forms
from django.contrib.auth import get_user_model

from watch_demo.core.form_mixins import DisabledFormMixin
from watch_demo.movies.models import Movie, Actor

UserModel = get_user_model()


class MovieBaseForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'genre', 'movie_poster', 'tagged_actors', 'year_of_release', 'description')
        # widgets = {
        #     'tagged_actors': forms.ChoiceField(
        #
        # #         queryset=Actor.objects.all(),
        # #         # to_field_name=Actor.full_name
        # #         # widget=forms.CheckboxSelectMultiple,
        #     ),
        # }


class MovieAddForm(MovieBaseForm):
    pass


class MovieEditForm(MovieBaseForm, DisabledFormMixin):
    pass


class ActorAddForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name')


