from django.shortcuts import render
from .models import Recipe
from django.core.cache import cache

def recipe(request):
    recipies = Recipe.objects.all()
    context = {'recipies': recipies}
    return render(request, 'recipe.html', context)

def recipe_single(request, pk):

    if cache.get(pk):
        recipe = cache.get(pk)
        print('hits the cache')
    else:
        recipe = Recipe.objects.get(id=pk)
        cache.set(pk, recipe, timeout=100)
        print('hits the db')
    context = {'recipe': recipe}
    return render(request, 'recipe_single.html', context)