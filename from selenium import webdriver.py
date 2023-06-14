from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update the path to your Chrome browser executable
    driver_path = r"C:\Users\DELL\AppData\Roaming\Microsoft\Windows\Network Shortcuts\chromedriver_win32\chromedriver.exe"  # Update the path to the ChromeDriver executable

    # Set the executable path using chrome_options
    options.add_argument(f"webdriver.chrome.driver={driver_path}")

    # Create the WebDriver instance
    browser = webdriver.Chrome(options=options)
    driver = browser

    # Navigate to Instagram
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    # Wait until the username input field is visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"))
    )
    username_input.send_keys(username)

    # Wait until the password input field is visible
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"))
    )
    password_input.send_keys(password)
    password_input.submit()

    # Handle "Not Now" if present
    try:
        not_now_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")))
        not_now_button.click()
    except:
        pass

    # Handle "Turn On Notifications" if present
    try:
        notification_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
        notification_button.click()
    except:
        pass

    # Wait until the first picture is visible
    first_picture = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[3]/div/div/div[1]/div/article[1]/div/div[2]/div/div/div/div[2]"))
    )
    first_picture.click()
    time.sleep(2)

    # Wait until the like button is visible and click it
    like_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[3]/div/div/div[1]/div/article[1]/div/div[3]/div/div/section[1]/span[1]/button"))
    )
    like_button.click()
    time.sleep(5)

    return "Liked first picture"

if __name__ == "__main__":
    app.run(debug=True)
