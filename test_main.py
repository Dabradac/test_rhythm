import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')
class TestMain:

    def test_main(self):
        self.driver.get('https://demoqa.com/')
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="item-1"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
        self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()
        element = self.driver.find_element(By.XPATH, '//*[@id="result"]/span[2]').text
        assert element == 'wordFile'
