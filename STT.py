# Speech To Text

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Setting up Chrome options with specific arguments
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")

# Setting up the Chrome driver with specified service and options
driver = webdriver.Chrome(service=Service(executable_path=r"C:\Users\chatu\OneDrive\Desktop\J.A.R.V.I.S\ChromeDriver\chromedriver.exe"), options=chrome_options)



# Creating the URL for the website using the current working directory
website = "https://allorizenproject1.netlify.app/"

# Opening the website in the Chrome browser
driver.get(website)

def listen():
    print("The Advance Speech To Text is Processing..")
    try:
        start_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'startButton')))
        start_button.click()
        print("Activated  Sir !")
        output_text = ""
        is_second_click = False
        while True:
            output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'output')))
            current_text = output_element.text.strip()
            if "Start Listening" in start_button.text and is_second_click:
                if output_text:
                    # print("User:", output_text)
                    is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True
            if current_text != output_text:
                output_text = current_text
                with open("web/input.txt", "w") as file:
                    file.write(output_text.lower())
                    print("User:", output_text)
            time.sleep(0.1)  
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("An error occurred:", e)


