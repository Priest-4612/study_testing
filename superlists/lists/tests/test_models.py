from django.test import TestCase

from lists.models import Item, List


class ItemModelTests(TestCase):
    '''тест модели элемента списка'''

    def test_saving_and_retrieving_items(self):
        text_item_1 = 'Первый (самый) элемент списка'
        text_item_2 = 'Элемент второй'

        current_list = List()
        current_list.save()

        first_item = Item()
        first_item.text = text_item_1
        first_item.list = current_list
        first_item.save()

        second_item = Item()
        second_item.text = text_item_2
        second_item.list = current_list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, current_list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, text_item_1)
        self.assertEqual(first_saved_item.list, current_list)
        self.assertEqual(second_saved_item.text, text_item_2)
        self.assertEqual(second_saved_item.list, current_list)
