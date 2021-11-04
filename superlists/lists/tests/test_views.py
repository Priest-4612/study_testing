from django.test import TestCase


class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_uses_home_template(self):
        '''тест: используется правильный шаблон'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
