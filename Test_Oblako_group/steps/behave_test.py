# -*- coding: utf-8 -*-
from behave import *
from selenium import webdriver
from behave import given, when, then, step  # pylint: disable=no-name-in-module

def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context)

@fixture
def browser_chrome(context, timeout=30, **kwargs):
    print("FIXTURE-SETUP: browser.chrome")
    context.browser = "chrome"
    yield
    print("FIXTURE-CLEANUP: browser.chrome")



@given("website {url}")
def step(context,url):
    context.browser=webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get('http://qa-assignment.oblakogroup.ru/board/:idhaykeminyan#')

@then("page include {text} {text_1} {text_2}")
def step(context, text,text_1,text_2):
    assert context.browser.find_element_by_css_selector('.title'.format(text))
    assert context.browser.find_element_by_css_selector('div.col-lg-4:nth-child(1) > div:nth-child(1) > h2:nth-child(1)'.format(text_1))
    context.browser.find_element_by_css_selector('#add_new_todo').click()
    assert context.browser.find_element_by_css_selector('.add_white_block > h3:nth-child(1)')
@then("push button with text '{text}'")
def step(context, text):
    assert context.browser.find_element_by_css_selector('#submit_add_todo'.format(text))
    context.browser.find_element_by_css_selector('#submit_add_todo').click()
    context.browser.quit()
