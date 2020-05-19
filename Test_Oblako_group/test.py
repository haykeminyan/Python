# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import Select
import string,random,logging,time
from random import choice, shuffle
from behave import given, when, then, step


logging.basicConfig(
    filename="result_final.log",
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    filemode='a',
    level=logging.INFO)


href_addr = 'http://qa-assignment.oblakogroup.ru/board/:idhaykeminyan'
ua = UserAgent()


@given('я загружаю страницу {}'.format(href_addr))
def step_impl(context):
    raise NotImplementedError(
        "STEP: Given я загружаю страницу {}".format(href_addr))


@then('долна открыться страница содержащая доску с задачами')
def step_impl(context):
    raise NotImplementedError(
        'STEP: Then долна открыться страница содержащая доску с задачами')


opts = Options()
user_random = str(ua.random)
opts.add_argument("user-agent={}".format(user_random))
opts.add_argument('--headless')
opts.add_argument('--no-sandbox')
opts.add_argument("--disable-setuid-sandbox")
opts.add_argument("--disable-extensions")
opts.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=opts)
browser.wait = WebDriverWait(browser, 10)
browser.get(href_addr)
logging.info('--------------------------------------------------------------------')
print(user_random)
logging.info('Current user-agent is {}'.format(user_random))
start = time.time()
browser.find_element_by_css_selector('#add_new_todo').click()
select_box = browser.find_element_by_class_name("new_todo_fields")
options = [x for x in select_box.find_elements_by_tag_name("option")]
list_of_categories = []
for element in options:
    list_of_categories.append(element.get_attribute("value"))
list_of_categories = [i for i in list_of_categories if i]

logging.info('Current list_of_categories are {}'.format(list_of_categories))
print('We have the list of categories: {}'.format(list_of_categories))
browser.find_element_by_css_selector('.select2-selection__arrow').click()
element = browser.find_element_by_css_selector(
    '#select2-select_category-results')
browser.execute_script("return arguments[0].scrollIntoView(true);", element)
select = Select(browser.find_element_by_class_name('select_category'))
last_word_in_list_category = 'Создать новый список'
select.select_by_visible_text(last_word_in_list_category)
browser.find_element_by_css_selector('.select2').click()
browser.find_element_by_css_selector('.select2-selection__arrow').click()
select_new = Select(browser.find_element_by_class_name('select_category'))


some_word_in_list_category = choice(list_of_categories)
logging.info('Chosen category is {}'.format(some_word_in_list_category))
print("Here is random word from categories: {}".format(some_word_in_list_category))
select_new = Select(browser.find_element_by_class_name('select_category'))
select_new.select_by_visible_text(some_word_in_list_category)
browser.find_element_by_css_selector('.select2').click()
lowercase_words = [random.choice(string.ascii_lowercase) for i in range(7)]
uppercase_words = [random.choice(string.ascii_uppercase) for i in range(7)]
union_words = lowercase_words + uppercase_words

shuffle(union_words)
res_for_title = ''.join(union_words)
logging.info('Title is {}'.format(res_for_title))
print("The title of the notepad is {}".format(res_for_title))
browser.find_element_by_css_selector('#project_title')
elem_1 = browser.find_element_by_css_selector('#project_title')
elem_1.click()
elem_1.send_keys(res_for_title)

shuffle(union_words)
res_for_text = ''.join(union_words)
logging.info('Text is: {}'.format(res_for_text))
print("The text of the notepad is {}".format(res_for_text))
browser.find_element_by_css_selector('#project_text')
elem = browser.find_element_by_css_selector('#project_text')
elem.click()
elem.send_keys(res_for_text)


browser.find_element_by_css_selector('#submit_add_todo').click()
end = time.time()

result_time = (float(end - start))
logging.info('Iteration of testing is {}'.format(result_time))
print("The result of testing is {}".format(result_time))
logging.info('--------------------------------------------------------------------')
