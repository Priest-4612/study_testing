from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    '''Домашняя страница'''
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    context = {'items': Item.objects.all()}
    return render(request, 'home.html', context)
