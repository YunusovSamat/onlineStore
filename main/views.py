from django.shortcuts import render


def index_view(request):
    template = 'main/index.html'

    return render(request, template)
