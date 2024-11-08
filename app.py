from flask import Flask, redirect, request, make_response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.service import Service as SafariService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

app = Flask(__name__)

# URL and credentials
LOGIN_URL = "https://www.panda.ie/d2d/"
PASSWORD = "PANDAD2DREP"

def get_browser_name(user_agent):
    user_agent = user_agent.lower()
    if "edg" in user_agent:  # Edge User-Agent contains 'edg'
        return "edge"
    elif "chrome" in user_agent and "edg" not in user_agent:
        return "chrome"
    elif "firefox" in user_agent:
        return "firefox"
    elif "safari" in user_agent and "chrome" not in user_agent:
        return "safari"
    else:
        raise ValueError("Unsupported browser detected")

def get_driver(browser_name):
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")  # Uncomment for headless mode

        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    elif browser_name == 'edge':
        options = EdgeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--headless")  # Uncomment for headless mode

        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")  # Uncomment for headless mode

        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    elif browser_name == 'safari':
        # Safari doesn't need additional options or services
        return webdriver.Safari()

    else:
        raise ValueError("Unsupported browser: {}".format(browser_name))

def accept_cookies(driver):
    try:
        # Find and click the 'Accept Cookies' button
        accept_button = driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
        driver.execute_script("arguments[0].click();", accept_button)
    except Exception as e:
        print("Cookies consent banner not found or already accepted", str(e))

def login_to_website(browser_name):
    driver = get_driver(browser_name)

    try:
        # Go to the login page
        driver.get(LOGIN_URL)

        # Accept cookies if the banner is present
        accept_cookies(driver)

        # Find the password input field and enter the password
        password_input = driver.find_element(By.NAME, 'post_password')
        password_input.send_keys(PASSWORD)

        # Find and click the login button
        login_button = driver.find_element(By.NAME, 'Submit')
        driver.execute_script("arguments[0].click();", login_button)

        # Wait for the next page to load
        time.sleep(5)  # Adjust the wait time as necessary

        # Get the current URL after logging in
        logged_in_url = driver.current_url

        # Extract cookies from Selenium
        cookies = driver.get_cookies()

        return logged_in_url, cookies  # Return the final logged-in URL and cookies

    finally:
        driver.quit()  # Close the browser

@app.route('/')
def login():
    # Get the User-Agent from the request headers
    user_agent = request.headers.get('User-Agent', '')

    try:
        # Determine the browser name based on User-Agent
        browser_name = get_browser_name(user_agent)

        # Trigger the login process and get the final logged-in URL and cookies
        logged_in_url, cookies = login_to_website(browser_name)

        # Create a response object
        response = make_response(redirect(logged_in_url))

        # Set cookies in the response
        for cookie in cookies:
            # Ensure cookies are set with appropriate attributes if needed
            response.set_cookie(cookie['name'], cookie['value'], path='/')

        return response
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=False)
