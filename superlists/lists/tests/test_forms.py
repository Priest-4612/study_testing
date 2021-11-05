from django.test import TestCase

from lists.models import Item
from .list_urls import LIST_URLS


class ItemCreateFormTests(TestCase):
    '''тест: проверяем форму для добавления новых записей'''

    def test_only_save_items_when_necessary(self):
        self.client.get(LIST_URLS['HOME'])
        self.assertEqual(Item.objects.count(), 0)

    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-запрос'''
        self.client.post(LIST_URLS['NEW'],
                         data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        '''тест: переадресация после post-запроса'''
        response = self.client.post(LIST_URLS['NEW'],
                                    data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], LIST_URLS['LIST'])