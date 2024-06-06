import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим имя')
    def set_name(self, name):
        self.set_field_by_locator(OrderPageLocators.name, name)

    @allure.step('Вводим фамилию')
    def set_surname(self, surname):
        self.set_field_by_locator(OrderPageLocators.surname, surname)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.set_field_by_locator(OrderPageLocators.address, address)

    @allure.step('Кликаем по полю "метро"')
    def click_metro_station(self):
        self.click_on_element(OrderPageLocators.metro_station)

    @allure.step('Проверяем кликабельность кнопки Комсомольская')
    def check_button_lubyanka(self):
        self.check_element_is_clickable(OrderPageLocators.lubyanka_station)

    @allure.step('Кликаем по станции "Комсомольская"')
    def click_metro_lubyanka_st(self):
        self.click_on_element(OrderPageLocators.lubyanka_station)

    @allure.step('Вводим номер телефона')
    def set_phone(self, phone):
        self.set_field_by_locator(OrderPageLocators.phone, phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next(self):
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step('Проверяем кликабельность кнопки "далее"')
    def check_button_next(self):
        self.check_element_is_clickable(OrderPageLocators.next_button)

    @allure.step('Проверяем кликабельность кнопки заказа')
    def check_button_order(self):
        self.check_element_is_clickable(OrderPageLocators.order_button)

    @allure.step('Кликаем по полю с датой')
    def click_date(self):
        self.click_on_element(OrderPageLocators.date)

    @allure.step('Кликаем по сегодняшней дате')
    def click_today(self):
        self.click_on_element(OrderPageLocators.today)

    @allure.step('Кликаем по срок аренды')
    def click_rental_period(self):
        self.click_on_element(OrderPageLocators.rental_period)

    @allure.step('Кликаем по желаемому периоду аренды')
    def click_rental_period_choose(self):
        self.click_on_element(OrderPageLocators.choose_rental_period)

    @allure.step('Выбираем цвет')
    def click_black_color(self):
        self.click_on_element(OrderPageLocators.black_color)

    @allure.step('Проверяем кликабельность кнопки заказа')
    def check_button_order(self):
        self.check_element_is_clickable(OrderPageLocators.order_button)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.order_button)

    @allure.step('Проверяем кликабельность кнопки "Да"')
    def check_button_yes_is_clickable(self):
        self.check_element_is_clickable(OrderPageLocators.yes_button)

    @allure.step('Кликаем на кнопку "Да"')
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.yes_button)

    @allure.step('Проверяем видимость кнопки "Проверить статус"')
    def check_visibility_of_button_status(self):
        self.check_element_is_visable(OrderPageLocators.status_button)

    @allure.step('Получаем текст кнопки "Проверить статус"')
    def text_in_button_status(self):
        return self.get_text_element(OrderPageLocators.status_button)

    @allure.step('Заполнение данных на форме "Для кого самокат"')
    def set_data_order(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_station()
        self.check_button_lubyanka()
        self.click_metro_lubyanka_st()
        self.set_phone(phone)

    @allure.step('Заполнение данных на форме "Про аренду"')
    def set_data_order_about_rent(self):
        self.check_button_order()
        self.click_date()
        self.click_today()
        self.click_rental_period()
        self.click_rental_period_choose()
        self.click_black_color()
        self.check_button_order()
        self.click_button_order()
        self.check_button_yes_is_clickable()
        self.click_button_yes()

    @allure.step('Проверяем кликабельность кнопки далее и кликаем"')
    def check_and_lick_check_button_next(self):
        self.check_button_next()
        self.click_next()
