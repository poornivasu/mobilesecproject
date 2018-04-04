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
    testName = 'Untitled'
    driver = None
    
    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '03ab1c13003c0097'
        self.dc['appPackage'] = 'com.weather.Weather'
        self.dc['appActivity'] = '.app.SplashScreenActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.dc)

    def testUntitled(self):
        self.driver.startActivity("com.weather.Weather", ".app.SplashScreenActivity")
        self.driver.find_element_by_xpath("xpath=//*[@class='android.widget.ImageButton']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='°F']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='background_ad_clickable']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='temperature_icon']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='back']").click()

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
