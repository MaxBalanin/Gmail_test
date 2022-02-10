import pytest
from selenium import webdriver

from GmailPagaes import GmailPages


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote(command_executor="http://192.168.1.92:4444")
    yield driver
    driver.quit()



