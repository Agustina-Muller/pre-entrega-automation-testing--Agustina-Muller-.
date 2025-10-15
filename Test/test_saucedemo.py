import pytest
from selenium.webdriver.common.by import By 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_driver, login_sauce


@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()



def test_validacion_login(driver):
    assert login_sauce(driver)
