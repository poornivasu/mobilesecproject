import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class Untitled(unittest.TestCase):
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
        self.dc['appPackage'] = 'com.cnn.mobile.android.phone'
        self.dc['appActivity'] = '.features.splash.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.dc)

    def testUntitled(self):
        self.driver.startActivity("com.cnn.mobile.android.phone", ".features.splash.SplashActivity")
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[1]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='CNN']").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[2]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=(//*[@class='android.widget.LinearLayout' and ./parent::*[@id='tabs']]/*/*[@id='verticalImageView' and @width>0])[3]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='shareNewsImg' and @width>0 and @height>0]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='back']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Watch Now']").click()
        self.driver.press_keycode(3) # home

    def tearDown(self):
        self.driver.quit()
        
    if __name__ == '__main__':
        unittest.main()

