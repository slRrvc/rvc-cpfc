from django.shortcuts import render


def index(request):
    return render(
        request,
        'rvccpf/pages/index.html'
    )
