from django.test import TestCase

from lists.models import Item, List
from .list_urls import LIST_URLS


class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_uses_home_template(self):
        '''тест: используется правильный шаблон'''
        response = self.client.get(LIST_URLS['HOME'])
        self.assertTemplateUsed(response, 'home.html')


class ListViewTests(TestCase):
    '''тест представления списка'''

    def test_uses_home_template(self):
        '''тест: используется правильный шаблон'''
        current_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=current_list)
        response = self.client.get(LIST_URLS['LIST']
                                   .format(id=current_list.id))
        self.assertTemplateUsed(response, 'list.html')

    def test_display_only_items_for_that_list(self):
        '''тест: отображаются все элементы списка'''
        item_1 = 'itemey 1'
        item_2 = 'itemey 2'
        other_item_1 = 'other itemey 1'
        other_item_2 = 'other itemey 2'

        current_list = List.objects.create()
        Item.objects.create(text=item_1, list=current_list)
        Item.objects.create(text=item_2, list=current_list)
        other_list = List.objects.create()
        Item.objects.create(text=other_item_1, list=other_list)
        Item.objects.create(text=other_item_2, list=other_list)
        response = self.client.get(LIST_URLS['LIST']
                                   .format(id=current_list.id))
        self.assertIn(item_1, response.content.decode())
        self.assertIn(item_2, response.content.decode())
        self.assertNotIn(other_item_1, response.content.decode())
        self.assertNotIn(other_item_2, response.content.decode())
