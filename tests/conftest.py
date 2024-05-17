import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture
def driver():
    options = Options()
    #options.add_argument('--headless')
    driver_service = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=driver_service, options=options)
    driver = webdriver.Remote(
        command_executor='http://172.17.0.2:4444/wd/hub',
        options=options
    )

    driver.maximize_window()
    yield driver
    driver.quit()