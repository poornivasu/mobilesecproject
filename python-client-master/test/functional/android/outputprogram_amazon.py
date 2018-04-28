# coding: utf-8
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
        dc = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = '03ab1c13003c0097'
        self.dc['appPackage'] = 'com.amazon.mShop.android.shopping'
        self.dc['appActivity'] = 'com.amazon.mShop.home.HomeActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.dc)

    def testUntitled(self):
		self.driver.find_element_by_xpath("xpath=//*[@id=\'action_bar_burger_icon\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Hello. Sign In\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Login. Already a customer? \' and @class=\'android.widget.RadioButton\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='p']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='o']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='o']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='r']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='n']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='i']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='.']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='b']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='a']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='v']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='y']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='a']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='@']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='g']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='m']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='a']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='i']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='l']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='.']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='c']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='o']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='m']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='k']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='a']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='l']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='y']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='a']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='n']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='i']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='p']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='o']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='o']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='r']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='n']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='i']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='m']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text='a']").click()
		self.driver.find_element_by_xpath("xpath=//*[@id=\'rs_search_src_text\']").click()
		
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Tap and long press to fling this item to your tray.\' and (./preceding-sibling::* | ./following-sibling::*)[./*[./*[./*[./*[@text=\'Wings of Fire: An Autobiography of APJ Abdul Kalam\']]]]]]").click()
		
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Submit\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Add to Cart\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@id=\'action_bar_cart_image\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Delete\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Settings\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Not vasu? Sign out\']").click()
		self.driver.find_element_by_xpath("xpath=//*[@text=\'Sign Out\']").click()
		self.driver.press_keycode(3) # home

    def tearDown(self):
        self.driver.quit()
        

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

