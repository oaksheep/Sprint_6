from selenium.webdriver.common.by import By


class MainPageLocators:

    order_button_lower = [By.CLASS_NAME, "Home_FinishButton__1_cWm"] # Блок с кнопкой заказа в нижней части главной страницы
    order_button_low = [By.CLASS_NAME, "Button_Button__ra12g Button_UltraBig__UU3Lp"] # Нижняя кнопка заказа
    samokat_blok = [By.CLASS_NAME, 'Home_Header__iJKdX'] # Блок "Самокат на пару дней"
    coolie_button = [By.ID, "rcc-confirm-button"] # Кнопка "Да все привыкли"
    samokat_logo = [By.XPATH, '//img[@alt="Scooter"]'] # Лого "Самокат"
    yandex_logo = [By.XPATH, '//img[@alt="Yandex"]'] # Лого "Яндекс"
    order_button = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()= "Заказать"]'] # "Заказать" из хэдера

    question_one = [By.ID, 'accordion__heading-0'] # Вопрос 1
    answer_one = [By.XPATH, "//div[@id='accordion__panel-0']//p"] # Ответ 1
    question_two = [By.ID, 'accordion__heading-1'] # Вопрос 2
    answer_two = [By.XPATH, "//div[@id='accordion__panel-1']//p"] # Ответ 2
    question_three = [By.ID, 'accordion__heading-2'] # Вопрос 3
    answer_three = [By.XPATH, "//div[@id='accordion__panel-2']//p"] # Ответ 3
    question_four = [By.ID, 'accordion__heading-3'] # Вопрос 4
    answer_four = [By.XPATH, "//div[@id='accordion__panel-3']//p"] # Ответ 4
    question_five = [By.ID, 'accordion__heading-4'] # Вопрос 5
    answer_five = [By.XPATH, "//div[@id='accordion__panel-4']//p"] # Ответ 5
    question_six = [By.ID, 'accordion__heading-5'] # Вопрос 6
    answer_six = [By.XPATH, "//div[@id='accordion__panel-5']//p"] # Ответ 6
    question_seven = [By.ID, 'accordion__heading-6'] # Вопрос 7
    answer_seven = [By.XPATH, "//div[@id='accordion__panel-6']//p"] # Ответ 7
    question_eight = [By.ID, 'accordion__heading-7'] # Вопрос 8
    answer_eight = [By.XPATH, "//div[@id='accordion__panel-7']//p"] # Ответ 8
