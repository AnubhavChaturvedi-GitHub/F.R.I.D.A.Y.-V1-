import time
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def configure_driver():
    """Configure and return a Chrome WebDriver instance."""
    ScriptDir = pathlib.Path().absolute()
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver



def login(driver):
    """Login to the website."""
    try:
        driver.get("https://pi.ai/")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/div/textarea")))
        print("Already logged in.")
        voice_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[2]/div[2]/div/div[2]")))
        voice_button.click()
    except:

        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/div/button')))
        next_button.click()

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/div/button')))
        next_button.click()
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/div/button')))
        next_button.click()




driver = configure_driver()
login(driver)
def chat(message):
    """Send a message and retrieve the response."""

    try:
        chat_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/div/textarea")))
        chat_input.send_keys(message)

        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/button")))
        send_button.click()

        time.sleep(2)

        result_area = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div")))
        result_text = result_area.text

        print("Result:", result_text)

        with open("web/response.txt", "a", encoding="utf-8") as file:
            file.write(result_text.lower())  # Append response to the file

    except :
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div/div[2]/button')))
        next_button.click()
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div/div/div/div/div[2]/button')))
        next_button.click()
        chat_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/div/textarea")))
        chat_input.send_keys(message)

        send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/button")))
        send_button.click()

        time.sleep(1)

        result_area = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div")))
        result_text = result_area.text

        print("Result:", result_text)

        with open("web/response.txt", "a", encoding="utf-8") as file:
            file.write(result_text.lower())  # Append response to the file





