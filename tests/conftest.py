import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = Options()
    #options.add_argument('--headless')
    driver_service = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=driver_service, options=options)
    driver = webdriver.Chrome(service=driver_service)
    # driver = webdriver.Remote(
    #     command_executor='http://localhost:4444/wd/hub',
    #     options=options
    # )

    driver.maximize_window()
    yield driver
    driver.quit()