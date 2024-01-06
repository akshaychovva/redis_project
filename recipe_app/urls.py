from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe),
    path('<int:pk>', views.recipe_single, name='recipe_single'),
]