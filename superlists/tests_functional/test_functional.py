import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    '''Тест нового посетителя'''

    def setUp(self):
        '''Установка'''
        PATH_CHROME_DRIVER = r'..\venv\Scripts\chromedriver'
        self.service = Service(PATH_CHROME_DRIVER)

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_later(self):
        '''тест: можно начать список и получить его позже'''
        self.service.start()
        self.browser = webdriver.Remote(self.service.service_url)
        self.browser.get(self.live_server_url)
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
        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table(
            '2: Сделать мушку из павлиньих перьев'
        )

        self.fail('Закончить тест!')
