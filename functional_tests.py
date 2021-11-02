from selenium import webdriver

PATH_CHROME_DRIVER = 'venv\Scripts\chromedriver.exe'
browser = webdriver.Chrome(PATH_CHROME_DRIVER)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
