import pytest
from selenium.webdriver.firefox import webdriver
from selenium import webdriver
import data
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    driver.delete_all_cookies()
    driver.get(data.Urls.url_main)
    yield driver
    driver.quit()

