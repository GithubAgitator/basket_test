import time

import pytest
from django.templatetags.i18n import language
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket'), "корзинка не найдена"




