import subprocess
import time

import pytest
from appium import webdriver

from tests.page.authorization_page import AuthorizationPage
from tests.page.login_page import LoginPage
from tests.page.main_page import MainPage
from tests.page.page_manager import PagesManager
from utils.android_utils import android_get_desired_cap

URL = 'http://localhost:4723/wd/hub'


@pytest.fixture(scope='session')
def setup_appium():

    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(setup_appium):
    driver = webdriver.Remote(URL, android_get_desired_cap())

    yield driver


@pytest.fixture(scope='session')
def page_manager(driver):
    return PagesManager(driver)


@pytest.fixture(scope='session')
def create_main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='session')
def create_login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='session')
def create_authorization_page(driver):
    return AuthorizationPage(driver)

@pytest.fixture(autouse=True)
def reset_tests(page_manager):
    pm = page_manager
    yield
    pm.reset_app()
