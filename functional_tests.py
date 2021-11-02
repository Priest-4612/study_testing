import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class NewVisitorTest(unittest.TestCase):
    '''Тест нового посетителя'''

    def setUp(self):
        '''Установка'''
        PATH_CHROME_DRIVER = r'venv\Scripts\chromedriver'
        self.service = Service(PATH_CHROME_DRIVER)

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        '''тест: можно начать список и получить его позже'''
        # Эдит слышала про крутое новое онлайн-приложение со
        # списком неотложных дел. Она решает оценить его
        # домашнюю страницу
        self.service.start()
        self.browser = webdriver.Remote(self.service.service_url)
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о
        # списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

        # Ей сразу же предлагается ввести элемент списка


if __name__ == '__main__':
    unittest.main(warnings='ignore')
