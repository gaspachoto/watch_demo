from django import forms

from watch_demo.common.models import MovieComment, MovieRating
from watch_demo.movies.models import Genre


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ('text',)
        labels = {
            'text': "Enter comment",
        }
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 35,
                    'rows': 2,
                    'placeholder': 'Add comment...'
                },
            ),
        }


class MovieRateForm(forms.ModelForm):
    class Meta:
        model = MovieRating
        fields = ('rating',)


# class SearchMoviesForm(forms.Form):
#     genre = forms.ChoiceField(
#         choices=Genre.choices(),
#         required=False,
#     )