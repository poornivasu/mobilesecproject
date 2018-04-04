import unittest
from appium import webdriver


from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import desired_capabilities

desired_caps = {}
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '6.0.1'
#desired_caps['deviceName'] = 'iPhone Simulator'
#desired_caps['app'] = PATH('../../apps/UICatalog.app.zip')

#self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


#from appium import webdriver


class MultiActionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    def testUntitled(self):
        self.driver.find_element_by_xpath("//*").click()

    def tearDown(self):
        self.driver.quit()




#class Untitled(unittest.TestCase):
#    reportDirectory = 'reports'
#    reportFormat = 'xml'
#    dc = {}
#    testName = 'Untitled'
#    driver = None
#    self.dc['reportDirectory'] = self.reportDirectory
#    self.dc['reportFormat'] = self.reportFormat
#    self.dc['testName'] = self.testName
#    self.dc['platformName'] = "android"
#    print "Calling the webserver"
#    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

#    def setUp(self):
#        print "setup"        
#
#    def testUntitled(self):
#        self.driver.find_element_by_xpath("//*").click()
#
#    def tearDown(self):
#        self.driver.quit()

#    if __name__ == '__main__':
#        unittest.main()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


