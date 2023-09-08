from selenium import webdriver


def create_driver(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    # Add more cases for other browsers


class DriverFactory:
    def create_driver(self, browser):
        pass
