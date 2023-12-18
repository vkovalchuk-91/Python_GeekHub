"""
Автоматизувати процес замовлення робота за допомогою Selenium
1. Отримайте та прочитайте дані з "https://robotsparebinindustries.com/orders.csv". Увага! Файл має бути прочитаний з
сервера кожного разу при запускі скрипта, не зберігайте файл локально.
2. Зайдіть на сайт "https://robotsparebinindustries.com/"
3. Перейдіть у вкладку "Order your robot"
4. Для кожного замовлення з файлу реалізуйте наступне:
    - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка його закриває.
    - оберіть/заповніть відповідні поля для замовлення
    - натисніть кнопку Preview та збережіть зображення отриманого робота. Увага! Зберігати треба тільки зображення
    робота, а не всієї сторінки сайту.
    - натисніть кнопку Order та збережіть номер чеку. Увага! Інколи сервер тупить і видає помилку, але повторне
    натискання кнопки частіше всього вирішує проблему. Дослідіть цей кейс.
    - переіменуйте отримане зображення у формат <номер чеку>_robot (напр. 123456_robot.jpg). Покладіть зображення в
    директорію output (яка має створюватися/очищатися під час запуску скрипта).
    - замовте наступного робота (шляхом натискання відповідної кнопки)

** Додаткове завдання (необов'язково)
    - окрім збереження номеру чеку отримайте також HTML-код всього чеку
    - збережіть отриманий код в PDF файл
    - додайте до цього файлу отримане зображення робота (бажано на одній сторінці, але не принципово)
    - збережіть отриманий PDF файл у форматі <номер чеку>_robot в директорію output. Окремо зображення робота зберігати
    не потрібно. Тобто замість зображень у вас будуть pdf файли які містять зображення з чеком.
"""
import base64
import os
import csv
import requests
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from xhtml2pdf import pisa


class RobotOrderProcessor:
    def __init__(self, base_dir, output_dir, base_url, csv_url):
        self.base_dir = base_dir
        self.output_dir = output_dir
        self.initialize_directory()
        self.orders_list = self.read_csv(csv_url)
        self.driver = self.initialize_driver(base_url)

    def initialize_directory(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        else:
            files = os.listdir(self.output_dir)
            for file in files:
                os.remove(os.path.join(self.output_dir, file))

    @staticmethod
    def read_csv(csv_url):
        response = requests.get(csv_url)
        if response.status_code == 200:
            csv_data = response.text.splitlines()
            csv_reader = csv.reader(csv_data)
            headers = next(csv_reader)
            data_list = []
            for row in csv_reader:
                data_dict = dict(zip(headers, row))
                data_list.append(data_dict)
            return data_list
        else:
            print(f"Помилка отриманння даних csv. Status code: {response.status_code}")
            return None

    @staticmethod
    def initialize_driver(base_url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--hide-scrollbars")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(base_url)
        return driver

    def click_order_another_robot_button(self):
        order_another_robot_button = self.wait_and_get_element((By.ID, "order-another"))
        self.driver.execute_script("arguments[0].click();", order_another_robot_button)

    def save_ticket_to_pdf(self):
        receipt_id = self.wait_and_get_element((By.CSS_SELECTOR, "p.badge-success")).text
        robot_image_elements = self.wait_and_get_element((By.ID, "robot-preview-image"))
        # robot_image_elements.screenshot(os.path.join(self.base_dir, f"output/{receipt_id}_robot.png"))
        # # Save ticket image
        screenshot = robot_image_elements.screenshot_as_png
        image_base64 = base64.b64encode(screenshot).decode("utf-8")
        image_html = f"<center><img src='data:image/png;base64,{image_base64}'></center><br>"
        receipt_html = self.wait_and_get_element((By.ID, "receipt")).get_attribute("outerHTML")
        pdf_file = os.path.join(self.base_dir, f'output/{receipt_id}_robot.pdf')
        with open(pdf_file, "w+b") as output_file:
            pisa.CreatePDF(image_html + receipt_html, dest=output_file)

    def click_order_button(self):
        order_button = self.wait_and_get_element((By.ID, "order"))
        self.driver.execute_script("arguments[0].click();", order_button)
        while self.check_alert():
            self.driver.execute_script("arguments[0].click();", order_button)

    def check_alert(self):
        try:
            self.wait_and_get_element((By.CLASS_NAME, "alert-danger"))
            print("Була помилка при натисканні кнопки замовлення, пробуємо ще раз!")
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def click_preview_button(self):
        preview_button = self.wait_and_get_element((By.ID, "preview"))
        self.driver.execute_script("arguments[0].click();", preview_button)

    def set_address(self, order_data):
        address_field = self.wait_and_get_element((By.ID, "address"))
        address_field.clear()
        address_field.send_keys(order_data["Address"])

    def set_legs(self, order_data):
        legs_field = self.wait_and_get_element(
            (By.CSS_SELECTOR, "input[placeholder='Enter the part number for the legs']"))
        legs_field.clear()
        legs_field.send_keys(order_data["Legs"])

    def set_body(self, order_data):
        self.driver.find_element(By.ID, f"id-body-{order_data['Body']}").click()

    def set_head(self, order_data):
        Select(self.driver.find_element(By.ID, "head")).select_by_index(order_data["Head"])

    def close_popup_if_present(self):
        try:
            self.wait_and_get_element((By.CSS_SELECTOR, "button.btn-dark")).click()
        except TimeoutException as ex:
            print(ex.msg)
            print("Спливаюче вікно не знайдено, продовжуємо дії")

    def wait_and_get_element(self, locator, timeout=1):
        try:
            return WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located(locator))
        except TimeoutException as ex:
            raise TimeoutException(f"Елемент з параметрами пошуку {locator} не знайдено") from ex

    def place_order(self, order_data):
        self.close_popup_if_present()
        self.set_head(order_data)
        self.set_body(order_data)
        self.set_legs(order_data)
        self.set_address(order_data)
        self.click_preview_button()
        self.click_order_button()
        self.save_ticket_to_pdf()
        self.click_order_another_robot_button()

    def process_orders(self):
        self.driver.get("https://robotsparebinindustries.com/")
        self.wait_and_get_element((By.LINK_TEXT, "Order your robot!")).click()
        for order in self.orders_list:
            print(f"Обробляємо замовлення {order}")
            self.place_order(order)

    def close_driver(self):
        self.driver.quit()


if __name__ == "__main__":
    BASE_DIR = os.getcwd()
    OUTPUT_DIR = 'output'
    BASE_URL = "https://robotsparebinindustries.com/"
    CSV_URL = "https://robotsparebinindustries.com/orders.csv"
    robot_order_processor = RobotOrderProcessor(BASE_DIR, OUTPUT_DIR, BASE_URL, CSV_URL)
    robot_order_processor.process_orders()
    robot_order_processor.close_driver()
