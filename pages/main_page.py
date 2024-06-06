import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Проверяем кликабельность кнопки заказа из header')
    def check_button_order_in_header_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.order_button)

    @allure.step('Проверяем кликабельность кнопки заказа внизу страницы')
    def check_button_order_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.order_button_lower)

    @allure.step('Проверяем кликабельность логотипа "Yandex"')
    def check_logo_yandex_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.yandex_logo)

    @allure.step('Кликаем по лого яндекса')
    def click_logo_yandex(self):
        self.click_on_element(MainPageLocators.yandex_logo)

    @allure.step('Кликаем по кнопке "Заказать" в header')
    def click_button_order_header(self):
        self.click_on_element(MainPageLocators.order_button)

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_button_order_div(self):
        self.click_on_element(MainPageLocators.order_button_lower)

    @allure.step('Кликаем по лого самоката')
    def click_logo_scooter(self):
        self.click_on_element(MainPageLocators.samokat_logo)

    @allure.step('Проверяем кликабельность и кликаем по кнопке заказа из header"')
    def check_and_click_order_header(self):
        self.check_button_order_in_header_is_clickable()
        self.click_button_order_header()