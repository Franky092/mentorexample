import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture(scope='function')
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument("--start-maximized")
    options.add_argument("disable-gpu")
    options.add_argument("--headless")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("allow-file-access-from-files")
    options.add_argument("use-fake-device-for-media-stream")
    options.add_argument("use-fake-ui-for-media-stream")
    options.add_argument("hide-scrollbars")
    options.add_argument("disable-features=VizDisplayCompositor")
    options.add_argument("disable-features=IsolateOrigins,site-per-process")
    options.add_argument("disable-popup-blocking")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("disable-notifications")
    return options

@pytest.fixture(scope='function')
def get_chrome_options_mobile():
    mobile_emulation = {"deviceName": "iPhone XR"}
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox");
    options.add_argument("--headless");
    options.add_argument("disable-gpu");
    options.add_experimental_option('excludeSwitches', ["enable-logging"]);
    options.add_experimental_option("mobileEmulation", mobile_emulation);
    return options

@pytest.fixture(scope='function')
def get_firefox_options():
    options = Options()
    options.add_argument('-headless')
    options.add_argument('--width=1920')
    options.add_argument('--height=1080')
    return options
@pytest.fixture(scope="function")
def get_webdriver(get_chrome_options, get_chrome_options_mobile,get_firefox_options, request):
    browser_name = request.param
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=get_chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox(options=get_firefox_options, executable_path=GeckoDriverManager().install())
    elif browser_name == "chromemobile":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=get_chrome_options_mobile)
    else:
        raise pytest.UsageError("browser_name should be chrome or firefox or chromemobile")
    yield driver
    print("\nquit browser..")
    driver.quit()



