from django.urls import path
from .views import calculate_recipe

urlpatterns = [
    path('<str:recipe_name>/', calculate_recipe, name='calculate_recipe'),
]
