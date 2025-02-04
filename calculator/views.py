from django.shortcuts import render
from django.http import HttpResponse
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
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def omlet_view(request,op1):

    recipe1 = DATA.get(op1)
    amount = int(request.GET.get("servings",1))
    if recipe1 == None:
        x ={}
        context = {'recipe': x}
    else:
        x = {}
        for r, g in recipe1.items():
            y = g * amount
            x[r] =y

            context = {'recipe':x}


    return render(request, 'index.html',context)



def hello(request):
    return render(request,'index.html')
