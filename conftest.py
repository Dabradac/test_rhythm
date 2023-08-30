import json

import pytest
from selenium import webdriver


@pytest.mark.usefixtures("runMode")
@pytest.fixture(scope='class')
def setup(request):
    with open('setting.json', 'r') as setting:
        setting = json.loads(setting.read())
    if setting['browser'] == "chrome":
        driver = webdriver.Chrome()
    elif setting['browser'] == "firefox":
        driver = webdriver.Firefox()
    else:
        print('Некорректно указан браузер в настройках!')
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield driver
    driver.close()