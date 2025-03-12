import argparse
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_driver(headless=True):
    options = Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("user-data-dir=/home/eirik/selenium_chromium_profile")
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    service = Service("/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=options)

parser = argparse.ArgumentParser()
parser.add_argument("--location", required=True, choices=["hjemmekontor", "school"], help="Specify location: hjemmekontor or school")
args = parser.parse_args()

message_to_send = "gm"
if args.location == "hjemmekontor":
    message_to_send = "gm(hk)"
elif args.location == "school":
    message_to_send = "gm"

print("Starting in headless mode.")
driver = create_driver(headless=True)
driver.get("https://discord.com/app")
time.sleep(2)
if "login" in driver.current_url:
    print("User not logged in. Switching to visible mode for manual login...")
    driver.quit()
    driver = create_driver(headless=False)
    driver.get("https://discord.com/login")
    print("Please log in to Discord within the next 60 seconds...")
    time.sleep(60)
else:
    print("User already logged in, proceeding silently.")

driver.get("https://discord.com/channels/1338508601043456093/1339586444045586573")
message_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][contenteditable='true']"))
)
message_input.send_keys(message_to_send)
message_input.send_keys(Keys.ENTER)
print("Check-in message sent: " + message_to_send)

if args.location == "school":
    log_path = os.path.join(os.path.expanduser("~"), "Documents", "kjoreliste_log.txt")
    with open(log_path, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Oppmøte (kjøreliste) registrert\n")
    print("Kjøreliste oppmøte logget.")

time.sleep(5)
driver.quit()
