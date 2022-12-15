from django.urls import path, include

from watch_demo.accounts.views import SignInView, SignUpView, SignOutView, UserDetailsView, UserEditView, \
    UserDeleteView, UserMovieListView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('movies/', UserMovieListView.as_view(), name='movies user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ]))
)