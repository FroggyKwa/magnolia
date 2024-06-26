from django.urls import path, include

from users import views

urlpatterns = [
    path('api/sign_in', views.SignInAPIView.as_view(),
         name="sign_in_and_get_token"),
    path('api/sign_in_with_token', views.CheckOneTimePasswordAPIView.as_view(),
         name="sign_in_with_token"),
    path('api/whoami', views.WhoAmI.as_view(), name="whoami"),
    path('api/logout', views.LogOutApiView.as_view(), name="logout"),
]
