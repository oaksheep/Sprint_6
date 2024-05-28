# Sprint 6
Aвто-тесты для сайта qa-scooter.praktikum-services.ru.
Проверка перехода на страницы при клике на логотопы в header: test_click_on_logo.py.
Проверка перехода при клике на логотип Yandex: test_logo_redirect_dzen_true.
Проверка перехода при клике на логотип Самокат: test_logo_go_to_start_page_true.
Вопрос-ответ на главной странице: test_main_page.py.
Проверка соответствия вопроса и ответа в разделе вопросы о важном: test_accordion.
Оформление заказа: test_order_page.py.
Проверка создания заказа через header: test_order_true.
Проверка открытия формы заказа по кнопки заказа внизу страницы: test_button_order_center_div.

Для работы нужны библиотеки: Selenium, Pytest, Allure.

Запуск автотестов: pytest -v
Запуск автотестов c формированием allure отчетов: pytest -v --alluredir=allure_results
Посмотреть вэб версию allure отчета: allure serve allure_results
#   S p r i n t _ 6  
 