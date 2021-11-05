from django.test import TestCase

from lists.models import Item
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
        response = self.client.get(LIST_URLS['LIST'])
        self.assertTemplateUsed(response, 'list.html')

    def test_display_all_items(self):
        '''тест: отображаются все элементы списка'''
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get(LIST_URLS['LIST'])
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())
