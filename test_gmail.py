# # -*- coding: UTF-8 -*-
import allure

from GmailPagaes import GmailPages
from conftest import browser

@allure.feature('Open page')
def test_mail(browser):
    gmail_page = GmailPages(browser)
    gmail_page.go_to_site()
    with allure.step('log in'):
        gmail_page.login('tmax35374@gmail.com')
        gmail_page.click_to_next_login_page()
        gmail_page.password('Retrowave12')
        gmail_page.click_to_next_login_page()
    with allure.step('send mail'):
        gmail_page.click_to_new_mail()
        gmail_page.input_send_email('tmax35374@gmail.com')
        gmail_page.input_send_body('Simbirsoft Тестовое задание')
        gmail_page.input_send_title('Simbirsoft Тестовое задание. Баланин')
    result = gmail_page.send_mail()
    assert result is True

