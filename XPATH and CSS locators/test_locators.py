from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_driver():
    driver_chrome = Chrome()
    driver_chrome.maximize_window()
    driver_chrome.get("https://twitter.com/")
    expected_title = driver_chrome.title
    assert expected_title == 'Твиттер. Здесь обсуждают всё, что происходит. / X'

    # XPATH locators
    assert driver_chrome.find_element(By.XPATH, '''//*[@id="react-root"]''')
    assert driver_chrome.find_element(By.XPATH, '''//div[4]''')
    assert driver_chrome.find_element(By.XPATH, '''//div[2]''')
    assert driver_chrome.find_element(By.XPATH, '''//main''')
    assert driver_chrome.find_element(By.XPATH, '''//div''')
    assert driver_chrome.find_element(By.XPATH, '''//div[1]''')
    assert driver_chrome.find_element(By.XPATH, '''//div[3]''')
    assert driver_chrome.find_element(By.XPATH, '''//a''')
    assert driver_chrome.find_element(By.XPATH, '''//span''')
    assert driver_chrome.find_element(By.XPATH, '''//a[4]''')
    assert driver_chrome.find_element(By.XPATH, '''//nav''')
    assert driver_chrome.find_element(By.XPATH, '''//a[1]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[2]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[3]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[5]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[6]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[7]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[8]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[9]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[10]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[11]''')

    complex_xpath_1 = '''//div[5]'''
    locator_xpath_1 = driver_chrome.find_element(By.XPATH, complex_xpath_1)
    elements_xpath_1 = locator_xpath_1.is_displayed()
    assert elements_xpath_1

    complex_xpath_2 = '''//a[12]'''
    locator_xpath_2 = driver_chrome.find_element(By.XPATH, complex_xpath_2)
    elements_xpath_2 = locator_xpath_2.is_displayed()
    assert elements_xpath_2

    complex_xpath_3 = '''//a[13]'''
    locator_xpath_3 = driver_chrome.find_element(By.XPATH, complex_xpath_3)
    elements_xpath_3 = locator_xpath_3.is_displayed()
    assert elements_xpath_3

    assert driver_chrome.find_element(By.XPATH, '''//a[14]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[15]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[16]''')
    assert driver_chrome.find_element(By.XPATH, '''//a[17]''')
    sleep(3)

    # CSS locators

    assert driver_chrome.find_element(By.CSS_SELECTOR, '''div''')
    assert driver_chrome.find_element(By.CSS_SELECTOR, '''a''')
    assert driver_chrome.find_element(By.CSS_SELECTOR, '''main''')
    assert driver_chrome.find_element(By.CSS_SELECTOR, '''span''')
    assert driver_chrome.find_element(By.CSS_SELECTOR, '''nav''')
