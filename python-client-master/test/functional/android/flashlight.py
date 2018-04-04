import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

import desired_capabilities
desired_caps = {}

class MultiActionTests(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'flashlight'
    driver = None
    
    def setUp(self):
        dc = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '03ab1c13003c0097'
        self.dc['appPackage'] = 'com.surpax.ledflashlight.panel'
        self.dc['appActivity'] = 'com.surpax.ledflashlight.FlashlightActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.dc)

    def testUntitled(self):
       # self.driver.startActivity("com.surpax.ledflashlight.panel", "com.surpax.ledflashlight.FlashlightActivity")
        self.driver.swipe(561, 1090, 561, 870, 280)
        self.driver.swipe(451, 229, 616, 232, 804)
        self.driver.swipe(390, 245, 674, 245, 420)
        self.driver.find_element_by_xpath("xpath=//*[@id='bt_settings']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Smart Charging']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='charging_display_settings_switch']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@contentDescription='Navigate up']")))
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Navigate up']").click()
        self.driver.press_keycode(3) # home

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
