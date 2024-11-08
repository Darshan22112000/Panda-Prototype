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
import json

# URL and credentials
LOGIN_URL = "https://www.panda.ie/d2d/"
PASSWORD = "PANDAD2DREP"

# Function to determine browser type from input (hardcoded or user input for simplicity)
def get_browser_name(choice="3"):
    # Ask the user to choose the browser or use a specific one
    print("Select the browser: 1. Chrome, 2. Firefox, 3. Edge, 4. Safari")
    # choice = input("Enter the number corresponding to your browser: ").strip()

    if choice == "1":
        return "chrome"
    elif choice == "2":
        return "firefox"
    elif choice == "3":
        return "edge"
    elif choice == "4":
        return "safari"
    else:
        raise ValueError("Unsupported browser detected")

# Function to initialize the driver for the chosen browser
def get_driver(browser_name):
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-blink-features=AutomationControlled")

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

        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)

    elif browser_name == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--start-maximized")

        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    elif browser_name == 'safari':
        # Safari doesn't need additional options or services
        return webdriver.Safari()

    else:
        raise ValueError("Unsupported browser: {}".format(browser_name))

# Function to accept cookies (if the popup appears)
def accept_cookies(driver):
    try:
        accept_button = driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
        driver.execute_script("arguments[0].click();", accept_button)
    except Exception as e:
        print("Cookies consent banner not found or already accepted", str(e))

# Function to perform the login process
def login_to_website(driver):
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

        # Get the current URL after logging in
        logged_in_url = driver.current_url

        # The browser stays open even after the function ends
        print("The browser will remain open. You can interact with it manually.")

    except Exception as e:
        print(f"Error occurred during login: {e}")
        driver.quit()  # Only close if an error occurs

# Main function to execute the script
if __name__ == "__main__":
    browser_name = get_browser_name()
    driver = get_driver(browser_name)
    login_to_website(driver)
    # No call to driver.quit() here, so the browser remains open after login
    # Keep the browser open
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        print("Exiting...")  # Clean exit if you stop the script manually
        driver.quit()  # Ensure to close the browser if you exit
