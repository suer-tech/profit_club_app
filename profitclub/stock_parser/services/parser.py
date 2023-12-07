from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
service = Service(executable_path=ChromeDriverManager().install())

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=service, options=chrome_options)


def get_price(self, name, url, xpath, xpath_proc):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    price = wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).text
    proc = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_proc))).text
    return [name, price, proc]


def format_number(self, input_str):
    # Удаляем все знаки "."
    input_str = input_str.replace('.', '')

    # Заменяем "," на "."
    input_str = input_str.replace(',', '.')

    # Оставляем два знака после разделителя "."
    if '.' in input_str:
        parts = input_str.split('.')
        if len(parts) == 2:
            input_str = f"{parts[0]}.{parts[1][:2]}"

    return input_str


def append_arr(self, arr, invest_stocks):
    for curr in invest_stocks:
        item = self.get_price(curr['name'], curr['url'], curr['xpath'], curr['xpath_proc'])
        arr.append(item)