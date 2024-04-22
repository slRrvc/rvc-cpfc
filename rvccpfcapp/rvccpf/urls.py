from django.urls import path
from rvccpf.views import index
appName = 'rvccpf'

urlpatterns = [
    path('', index, name='index'),
]
