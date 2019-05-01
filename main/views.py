from django.shortcuts import render


def index_view(request):
    template = 'main/index.html'

    return render(request, template)
    # В конце заменить текст категорий и подкатегорий в меню на данные в бд
