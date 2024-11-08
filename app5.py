from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import threading
from mapping import Map_values
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import threading

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'e0cde9daba88d7'  # Your email
app.config['MAIL_PASSWORD'] = '0619af0463c651'  # Your email password
app.config['MAIL_DEFAULT_SENDER'] = 'fieldsales@panda.ie'

mail = Mail(app)

LOGIN_URL = "https://www.panda.ie/d2d/"
PASSWORD = "PANDAD2DREP"

AGENTS = ["Darshan", "Aayush", "Kashish"]
AREAS = ["Tullamore", "Meath", "South Dublin"]
PLANS = ["Tullamore €17/month 65kg (€120/year)", "Navan €13/month 50 kg (€120 for the Year)",
         "South Dublin €13 (€99) 42kg"]

def get_driver(browser_name):
    if browser_name == 'chrome':
        options = ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--headless")  # Uncomment for headless mode

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
        # options.add_argument("--headless")  # Uncomment for headless mode
        return webdriver.Safari()

    else:
        raise ValueError("Unsupported browser: {}".format(browser_name))



def send_email(first_name, last_name, email, area, plan, login_link):
    msg = Message('Sign Up to Panda',
                  recipients=[email])
    msg.body = f"Hi {first_name} {last_name},\n\nClick the link below to Join Panda:\n\n{login_link}"
    msg.html = f"""
    <p>Hi {first_name} {last_name},</p>
    <p>Click the link below to Sign Up to Panda:</p>
    <p>Area: {area}, Plan: {plan}</p>
    <a href="{login_link}">Login to Panda</a>
    """
    mail.send(msg)

def get_browser_name(user_agent):
    user_agent = user_agent.lower()
    if "edg" in user_agent:
        return "edge"
    elif "chrome" in user_agent and "edg" not in user_agent:
        return "chrome"
    elif "firefox" in user_agent:
        return "firefox"
    elif "safari" in user_agent and "chrome" not in user_agent:
        return "safari"
    else:
        return None  # Return None for unsupported browsers

def accept_cookies(driver):
    try:
        accept_button = driver.find_element(By.XPATH, '//*[@id="wt-cli-accept-all-btn"]')
        driver.execute_script("arguments[0].click();", accept_button)
    except Exception as e:
        print("Cookies consent banner not found or already accepted", str(e))

def login_to_website(browser_name, agent, area, plan):
    driver = get_driver(browser_name)
    agent = Map_values.inverse_agent_mapping[agent]
    area = Map_values.inverse_area_mapping[area]
    plan = Map_values.inverse_plan_mapping[plan]

    try:
        driver.get(LOGIN_URL)
        accept_cookies(driver)

        password_input = driver.find_element(By.NAME, 'post_password')
        password_input.send_keys(PASSWORD)

        login_button = driver.find_element(By.NAME, 'Submit')
        driver.execute_script("arguments[0].click();", login_button)

        # Use JavaScript to set the agent value and disable the dropdown
        script = f"""
                        // Set agent value and disable
                        let agentField = document.querySelector('#input_11_20');
                        agentField.value = '{agent}';
                        agentField.disabled = true;
                        agentField.style.backgroundColor = '#e0e0e0';  // Greyed out

                        // Set area value and disable
                        let areaField = document.querySelector('#input_11_21');  // Assuming the ID for area dropdown
                        areaField.value = '{area}';
                        areaField.disabled = true;
                        areaField.style.backgroundColor = '#e0e0e0';  // Greyed out

                        // Set plan value and disable
                        let planField = document.querySelector('#input_11_22');  // Assuming the ID for plan dropdown
                        planField.value = '{plan}';
                        planField.disabled = true;
                        planField.style.backgroundColor = '#e0e0e0';  // Greyed out

                        localStorage.setItem('agentField', '{agent}');
                        localStorage.setItem('areaField', '{area}');
                        localStorage.setItem('planField', '{plan}');
                        localStorage.setItem('fieldsDisabled', 'true');
                        """
        driver.execute_script(script)

        logged_in_url = driver.current_url
        print("Logged in successfully. The browser will remain open.")
        return logged_in_url

    except Exception as e:
        print(f"Error occurred during login: {e}")
        driver.quit()  # Only close if an error occurs

@app.route('/')
def index():
    return render_template('index.html', agents=AGENTS, areas=AREAS, plans=PLANS)

@app.route('/login', methods=['GET'])
def login():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    agent = request.args.get('agent')
    area = request.args.get('area')
    plan = request.args.get('plan')

    login_link = f"http://localhost:5000/perform-login?agent={agent}&area={area}&plan={plan}"

    # thread = threading.Thread(target=login_to_website, args=('chrome', agent, area, plan))
    # thread.start()

    send_email(first_name, last_name, email, area, plan, login_link)

    return jsonify({"message": "SignUp link has been sent to your email."})

# @app.route('/perform-login', methods=['GET'])
def perform_login():
    # Get query parameters
    agent = request.args.get('agent')
    area = request.args.get('area')
    plan = request.args.get('plan')

    user_agent = request.headers.get('User-Agent', '')
    browser_name = get_browser_name(user_agent)
    if browser_name is None:
        return jsonify({"error": "Unsupported browser detected. Please use Chrome, Firefox, Edge, or Safari."}), 400

    # Run the login process in a separate thread
    thread = threading.Thread(target=login_to_website, args=(browser_name, agent, area, plan))
    thread.start()
    return jsonify({"message": "You're being redirected to Sign Up page."})

if __name__ == "__main__":
    app.run(debug=False, threaded=True)
