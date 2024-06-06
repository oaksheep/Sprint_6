from selenium.webdriver.common.by import By


class OrderPageLocators:

    name = [By.XPATH, '//input[@placeholder="* Имя"]'] # Поле ввод имени
    surname = [By.XPATH, '//input[@placeholder="* Фамилия"]'] # Поле ввод фамилии
    address = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'] # Поле ввод адреса
    metro_station = [By.XPATH, '//input[@placeholder="* Станция метро"]'] # Поле выбора станции
    phone = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'] # Ввод телефона
    date = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'] # Поле выбора даты доставки
    today = [By.CLASS_NAME, 'react-datepicker__day--today'] # Текущая дата
    rental_period = [By.CLASS_NAME, 'Dropdown-placeholder'] # Поле выбора периода аренды
    choose_rental_period = [By.XPATH, '//div[@class = "Dropdown-option" and text()="трое суток"]']  # Время аренды
    black_color = [By.ID, 'black'] # Чекбокс для черного цвета
    next_button = [By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()= "Далее"]'] # Кнопка "Далее"
    order_button = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()= "Заказать"]']  # Кнопка "Заказать"
    yes_button = [By.XPATH, './/button[text()= "Да"]'] # Кнопка "Да"
    status_button = [By.XPATH, './/button[text()= "Посмотреть статус"]'] # Кнопка "Посмотреть статус"
    lubyanka_station = [By.XPATH, f'//div[text()= "Лубянка"]'] # Станция "Лубянка" в выпадающем списке
