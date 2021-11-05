from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    '''Домашняя страница'''
    return render(request, 'home.html')


def view_list(request):
    context = {'items': Item.objects.all()}
    return render(request, 'list.html', context)


def new_list(request):
    '''новый список'''
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/one-list/')
