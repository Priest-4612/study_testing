import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    '''Тест нового посетителя'''

    def setUp(self):
        '''Установка'''
        PATH_CHROME_DRIVER = r'..\venv\Scripts\chromedriver'
        self.service = Service(PATH_CHROME_DRIVER)

    def tearDown(self):
        '''демонтаж'''
        self.service.stop()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def add_new_element(self, text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(text)
        inputbox.send_keys(Keys.ENTER)

    def test_can_start_a_list_for_one_user(self):
        '''тест: можно начать список для одного пользователя'''
        self.service.start()
        self.browser = webdriver.Remote(self.service.service_url)
        self.browser.get(self.live_server_url)

        self.add_new_element('Купить павлиньи перья')
        self.wait_for_row_in_list_table('1: Купить павлиньи перья')
        self.add_new_element('Сделать мушку из павлиньих перьев')
        self.wait_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')

    # def test_multiple_users_can_start_lists_at_different_urls(self):
    #     '''
    #         тест: многочисленные пользователи могут начать списки по разным url
    #     '''

    #     self.service.start()
    #     self.browser = webdriver.Remote(self.service.service_url)
    #     self.browser.get(self.live_server_url)
    #     self.add_new_element('Купить павлиньи перья')
    #     self.wait_for_row_in_list_table('1: Купить павлиньи перья')

    #     edith_list_url = self.browser.current_url
    #     self.assertRegex(edith_list_url, '/lists/.+')
    #     self.service.stop()

    #     self.service.start()
    #     self.browser = webdriver.Remote(self.service.service_url)
    #     self.browser.get(self.live_server_url)
    #     page_text = self.browser.find_element_by_tag_name('body').text
    #     self.assertNotIn('Купить павлиньи перья', page_text)
    #     self.assertNotIn('Сделать мушку из павлиньих перьев', page_text)
    #     self.add_new_element('Купить молоко')
    #     self.wait_for_row_in_list_table('1: Купить молоко')

    #     francis_list_url = self.browser.current_url
    #     self.assertRegex(francis_list_url, '/lists/.+')
    #     self.assertNotIn('Купить павлиньи перья', page_text)
    #     self.assertNotEqual(francis_list_url, edith_list_url)

    #     page_text = self.browser.find_element_by_tag_name('body').text
    #     self.assertNotIn('Купить павлиньи перья', page_text)
    #     self.assertIn('Купить молоко')
