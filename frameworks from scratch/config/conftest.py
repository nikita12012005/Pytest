import pytest
from driver_factory import DriverFactory
from config_reader import ConfigReader


@pytest.fixture(scope="session")
def config():
    return ConfigReader("config_file.ini")


@pytest.fixture(scope="function")
def driver(config):
    browser = config.get("WebAppConfig", "browser")
    driver_factory = DriverFactory()
    driver = driver_factory.create_driver(browser)
    yield driver
    driver.quit()
