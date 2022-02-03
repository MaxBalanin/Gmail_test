import pytest
from selenium import webdriver
from GmailPagaes import GmailTester



@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()


