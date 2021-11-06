from django.test import TestCase

from lists.models import Item, List
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
        current_list = List.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                         LIST_URLS['LIST'].format(id=current_list.id))


class NewItemTests(TestCase):
    '''тест нового элемента списка'''

    def test_can_save_a_POST_request_to_an_existing_list(self):
        '''тест: можно сохранить post-запрос в существующий список'''
        new_item_text = 'A new item for an existing list'
        other_list = List.objects.create()
        current_list = List.objects.create()

        self.client.post(
            LIST_URLS['ADD_ITEM'].format(id=current_list.id),
            data={'item_text': new_item_text}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, new_item_text)
        self.assertEqual(new_item.list, current_list)
        self.assertNotEqual(new_item.list, other_list)

    def test_redirects_to_list_view(self):
        '''тест: переадресуется в представление списка'''
        new_item_text = 'A new item for an existing list'
        current_list = List.objects.create()
        response = self.client.post(
            LIST_URLS['ADD_ITEM'].format(id=current_list.id),
            data={'item_text': new_item_text}
        )
        self.assertRedirects(response,
                             LIST_URLS['LIST'].format(id=current_list.id))
