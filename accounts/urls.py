from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profile'),
    path('reset', views.UserPasswordResetView.as_view(), name='reset_password'),
    path('reset/done/', views.UserPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/complete/', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('follow/<int:user_id>/', views.UserFollowView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/',
         views.UserUnfollowView.as_view(), name='unfollow'),
    path('followers/<int:user_id>/',
         views.ShowFollowersView.as_view(), name='followers'),
    path('following/<int:user_id>/',
         views.ShowFollowingView.as_view(), name='followings'),
    path('edit_user/', views.EditUserView.as_view(), name='edit_user'),
]
