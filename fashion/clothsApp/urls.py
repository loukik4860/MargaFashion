from django.urls import path
from . import views


urlpatterns=[
    path('home/', views.HomeView),
    path('mens/', views.MensView),
    path('ladies/',views.LadiesView),
    path('kids/',views.KidsView),
    path('Assr/',views.Accessories),
    path('signup/',views.SignUpView)

]