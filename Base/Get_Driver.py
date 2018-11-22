from appium import webdriver


class Get_Driver:
    def get_driver(self,Package,Activity):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.0.0'
        self.desired_caps['deviceName'] = 'HUAWEI nova2'
        self.desired_caps['appPackage'] = Package
        self.desired_caps['appActivity'] = Activity
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] = True
        return webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)