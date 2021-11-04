import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


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
        self.service.start()
        self.browser = webdriver.Remote(self.service.service_url)
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)

        header_test = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_test)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Купить павлиньи перья')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(rows.text == '1: Купить павлиньи перья' for row in rows),
            "Новый элемент списка не появился в таблице"
        )

        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
