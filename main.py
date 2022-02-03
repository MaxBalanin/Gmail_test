# # -*- coding: UTF-8 -*-
from GmailPagaes import GmailTester
from conftest import browser

def test_mail(browser):
    gmail_page = GmailTester(browser)
    gmail_page.go_to_site()
    gmail_page.login()
    gmail_page.click_to_next_login_page()
    gmail_page.password()
    gmail_page.click_to_next_login_page()
    gmail_page.click_to_new_mail()
    gmail_page.input_send_email()
    gmail_page.input_send_body()
    gmail_page.input_send_title()
    gmail_page.send_mail()