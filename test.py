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
from bs4 import BeautifulSoup
import requests
import time
from itertools import cycle
from fake_useragent import UserAgent
from collections import Counter
import shutil
import os
import pandas as pd
import logging
from selenium.webdriver.support.ui import Select
import string
import random
from random import choice, shuffle
href_addr = 'http://qa-assignment.oblakogroup.ru/board/:idhaykeminyan'
ua = UserAgent()
headers = {'User-Agent': str(ua.chrome)}

browser = webdriver.Chrome()
browser.wait = WebDriverWait(browser, 10)
browser.get(href_addr)
actions = ActionChains(browser)
# def switcher(href_addr):
#     while True:
#         try:
#             ip=requests.get(href_addr,headers=headers,timeout=10).content
#             break
#         except Exception as errors:
#             logging.info('--------------------------------------------------------------------------')
#             logging.error('{}'.format(errors))
#             continue
#     return ip


# for i in range(10):

#     browser.find_element_by_css_selector('#add_new_todo').click()
#     elem=browser.find_element_by_css_selector('#project_text')
#     elem.click()
#     elem.send_keys(res)
#     browser.find_element_by_css_selector('#submit_add_todo').click()
for i in range(10):
    browser.find_element_by_css_selector('#add_new_todo').click()
    select_box = browser.find_element_by_class_name("new_todo_fields")
    options = [x for x in select_box.find_elements_by_tag_name("option")]
    list_of_categories = []
    for element in options:
        list_of_categories.append(element.get_attribute("value"))
    list_of_categories = [i for i in list_of_categories if i]
    print(list_of_categories)

    browser.find_element_by_css_selector('.select2-selection__arrow').click()
    element = browser.find_element_by_css_selector(
        '#select2-select_category-results')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", element)
    select = Select(browser.find_element_by_class_name('select_category'))
    last_word_in_list_category = 'Создать новый список'
    select.select_by_visible_text(last_word_in_list_category)
    browser.find_element_by_css_selector('.select2').click()
    browser.find_element_by_css_selector('.select2-selection__arrow').click()
    select_new = Select(browser.find_element_by_class_name('select_category'))
    some_word_in_list_category = choice(list_of_categories)
    print(some_word_in_list_category)
    select_new = Select(browser.find_element_by_class_name('select_category'))
    select_new.select_by_visible_text(some_word_in_list_category)
    browser.find_element_by_css_selector('.select2').click()
    lowercase_words = [random.choice(string.ascii_lowercase) for i in range(7)]
    uppercase_words = [random.choice(string.ascii_uppercase) for i in range(7)]
    union_words = lowercase_words+uppercase_words
    shuffle(union_words)
    res = ''.join(union_words)
    time.sleep(2)
    elem = browser.find_element_by_css_selector('#project_text')
    elem.click()
    elem.send_keys(res)
    browser.find_element_by_css_selector('#project_title')
    elem_1 = browser.find_element_by_css_selector('#project_title')
    elem_1.click()
    elem_1.send_keys(res)
    browser.find_element_by_css_selector('#submit_add_todo').click()
    time.sleep(2)
#
# ##Если хотим выбрать какой-то последний элемент, тогда скроллим
# element =browser.find_element_by_css_selector('#select2-select_category-results')
# browser.execute_script("return arguments[0].scrollIntoView(true);",element)
# #
# select = Select(browser.find_element_by_class_name('select_category'))
# select.select_by_visible_text("Семья")
# browser.find_element_by_css_selector('.select2').click()
# lowercase_words=[random.choice(string.ascii_lowercase) for i in range(7)]
# uppercase_words=[random.choice(string.ascii_uppercase) for i in range(7)]
# union_words=lowercase_words+uppercase_words
# shuffle(union_words)
# res=''.join(union_words)

# elem=browser.find_element_by_css_selector('#project_text')
# elem.click()
# elem.send_keys(res)
# browser.find_element_by_css_selector('#submit_add_todo').click()
# dw
