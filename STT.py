from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd

# Setting up Chrome options with specific arguments
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")

# Setting up the Chrome driver with WebDriverManager and options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Creating the URL for the website using the current working directory
website = "https://allorizenproject1.netlify.app/"

# Opening the website in the Chrome browser
driver.get(website)

Recog_File = f"{getcwd()}\\web\\input.txt"

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
                    is_second_click = False
            elif "Listening..." in start_button.text:
                is_second_click = True
            if current_text != output_text:
                output_text = current_text
                with open(Recog_File, "w") as file:  
                    file.write(output_text.lower())
                    print("User:", output_text)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("An error occurred:", e)
