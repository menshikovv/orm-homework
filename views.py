from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
},

def calculate_recipe(request, recipe_name):
    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
    except ValueError:
        servings = 1

    recipe_data = DATA.get(recipe_name, {})
    context = {'recipe': {}}

    for ingredient, amount_per_serving in recipe_data.items():
        total_amount = amount_per_serving * servings
        context['recipe'][ingredient] = total_amount

    return render(request, 'calculator/index.html', context)
