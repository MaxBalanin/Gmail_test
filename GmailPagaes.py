import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class GmailLocators:

    LOCATOR_GMAIL_USERNAME = (By.NAME, 'identifier')
    LOCATOR_GMAIL_PASSVORD = (By.NAME, 'password')
    LOCATOR_GMAIL_NEXT_BUTTON = (By.CLASS_NAME, 'VfPpkd-vQzf8d')
    LOCATOR_GMAIL_INBOX_TITLE = (By.CLASS_NAME, 'bqe')
    LOCATOR_GMAIL_NEW_MAIL = (By.CLASS_NAME, 'aic')
    LOCATOR_GMAIL_SENDER_EMAIL = (By.CSS_SELECTOR, "input[peoplekit-id='BbVjBd']")
    LOCATOR_GMAIL_SENDER_TITLE = (By.NAME, 'subjectbox')
    LOCATOR_GMAIL_SENDER_BODY = (By.CSS_SELECTOR, "div[aria-label='Текст письма']")
    LOCATOR_GMAIL_SEND_MAIL = (By.CLASS_NAME, 'dC')


class GmailPages(BasePage):

    def login(self, email):
        login_input = self.find_element(GmailLocators.LOCATOR_GMAIL_USERNAME)
        login_input.send_keys(email)

    def click_to_next_login_page(self):
        self.find_element(GmailLocators.LOCATOR_GMAIL_NEXT_BUTTON).click()

    def password(self, password):
        pass_input = self.find_element(GmailLocators.LOCATOR_GMAIL_PASSVORD)
        pass_input.send_keys(password)

    def count_mails(self, desired_text):
        title_mails = self.find_elements(GmailLocators.LOCATOR_GMAIL_INBOX_TITLE)
        title_name = [x.text for x in title_mails if x.text == desired_text]
        count_mail = len(title_name)
        return count_mail

    def click_to_new_mail(self):
        self.find_element(GmailLocators.LOCATOR_GMAIL_NEW_MAIL).click()

    def input_send_email(self, email):
        sender_email = self.find_element(GmailLocators.LOCATOR_GMAIL_SENDER_EMAIL)
        sender_email.send_keys(email)

    def input_send_title(self, message):
        sender_title = self.find_element(GmailLocators.LOCATOR_GMAIL_SENDER_TITLE)
        sender_title.send_keys(message)

    def input_send_body(self, desired_text):
        sender_body = self.find_element(GmailLocators.LOCATOR_GMAIL_SENDER_BODY)
        sender_body.send_keys(self.count_mails(desired_text))

    def send_mail(self):
        self.find_element(GmailLocators.LOCATOR_GMAIL_SEND_MAIL).click()
        return True