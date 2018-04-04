import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import desired_capabilities

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1


class MultiActionTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        #self.desired_caps['platformName'] = "android"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#class Untitled(unittest.TestCase):
#    reportDirectory = 'reports'
#    reportFormat = 'xml'
#    dc = {}
#    testName = 'Untitled'
#    driver = None

#    def setUp(self):
#        self.dc['reportDirectory'] = self.reportDirectory
#        self.dc['reportFormat'] = self.reportFormat
#        self.dc['testName'] = self.testName
#        self.dc['platformName'] = "android"
#
#        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def testUntitled(self):
        self.driver.find_element_by_xpath("//*").click()

    def tearDown(self):
        self.driver.quit()

#    if __name__ == '__main__':
#        unittest.main()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MultiActionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
