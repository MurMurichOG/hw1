from django.views import generic
from .models import Clothes


class MaleClothes(generic.ListView):
    template_name = 'clothes/male.html'
    model = Clothes
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(tags__name='#для мужчин').order_by('-id')


class FemaleClothes(generic.ListView):
    template_name = 'clothes/female.html'
    model = Clothes
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(tags__name='#для женщин').order_by('-id')


class PensioneerCLothes(generic.ListView):
    template_name = 'clothes/pensioneer.html'
    model = Clothes
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(tags__name='#для пенсионеров').order_by('-id')


class KidsClothes(generic.ListView):
    template_name = 'clothes/kids.html'
    model = Clothes
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(tags__name='#для детей').order_by('-id')

