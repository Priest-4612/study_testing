from django.shortcuts import redirect, render

from lists.models import Item, List


def home_page(request):
    '''Домашняя страница'''
    return render(request, 'home.html')


def view_list(request, list_id):
    current_list = List.objects.get(id=list_id)
    context = {
        'items': Item.objects.filter(list=current_list),
        'current_list': current_list.id
    }
    return render(request, 'list.html', context)


def new_list(request):
    '''новый список'''
    current_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=current_list)
    return redirect(f'/lists/{current_list.id}/')


def add_item(request, list_id):
    current_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=current_list)
    return redirect(f'/lists/{current_list.id}/')
