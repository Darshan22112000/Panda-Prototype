from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time

app = Flask(__name__)

# Global variable for the WebDriver instance
driver = None

def start_driver():
    global driver
    options = ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode if you don't need a UI
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.panda.ie/d2d/")  # Navigate to the login page initially

def stop_driver():
    global driver
    if driver is not None:
        driver.quit()
        driver = None

@app.route('/start', methods=['POST'])
def start():
    # Start the WebDriver in a separate thread
    threading.Thread(target=start_driver).start()
    return jsonify({"message": "WebDriver started."}), 200

@app.route('/login', methods=['POST'])
def login():
    global driver
    if driver is None:
        return jsonify({"error": "WebDriver is not running."}), 400

    password = request.json.get('password')
    try:
        # Accept cookies if needed
        accept_button = driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
        driver.execute_script("arguments[0].click();", accept_button)
        time.sleep(1)  # Wait for the cookies banner to disappear

        # Enter the password and click the login button
        password_input = driver.find_element(By.NAME, 'post_password')
        password_input.send_keys(password)

        login_button = driver.find_element(By.NAME, 'Submit')
        driver.execute_script("arguments[0].click();", login_button)

        time.sleep(5)  # Wait for the login process to complete

        # Check if login was successful by checking the URL or page content
        logged_in_url = driver.current_url
        return jsonify({"message": "Logged in successfully.", "url": logged_in_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stop', methods=['POST'])
def stop():
    stop_driver()
    return jsonify({"message": "WebDriver stopped."}), 200

if __name__ == '__main__':
    app.run(debug=True)
